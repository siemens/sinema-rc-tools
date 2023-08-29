#!/usr/bin/python3
# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

# pylint: disable=line-too-long, c-extension-no-member, global-statement, broad-except

"""

Name:
    postgresDB_example.py

Description:
    Example to push user log in to in postgres DB


Author:
    Siemens Support

Copyright:
    Copyright (c) 2022 SIEMENS AG

"""
import datetime
from time import sleep
import psycopg2
from sinemarc_api.lib.srcapi_core import src_api
from sinemarc_api.lib.definitions import STATUS_OK
import argparse
import logging


DATABASE_TABLE = 'userlog'

SQL_ADD_ENTRY = '''INSERT INTO {} (id, time, username, endpoint,destinationPort, duration, usage, packages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO Update SET time = EXCLUDED.time, username = EXCLUDED.username, endpoint = EXCLUDED.endpoint, duration = EXCLUDED.duration, usage = EXCLUDED.usage, packages = EXCLUDED.packages'''.format(DATABASE_TABLE)
SQL_CREATE_TABLE =  '''CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,time TIMESTAMPTZ, username TEXT NOT NULL, endpoint TEXT NOT NULL, destinationPort INTEGER NOT NULL, duration REAL, usage bigint, packages INTEGER) ;'''.format(DATABASE_TABLE)
SQL_SELECT_HIGHEST_ID = '''SELECT MAX(id) FROM {}'''.format(DATABASE_TABLE)

#Example
# This will push user log to postgres
parser = argparse.ArgumentParser(
    description='Example script, which will poll the user log every 60s and update the defined database')
parser.add_argument(
    '-a', '--addr', help='Address of SINEMA RC Server', nargs='?')
parser.add_argument(
    '-po', '--port', help='Address port of SINEMA RC Server', nargs='?', default=443)
parser.add_argument(
    '-u', '--user', help='User name SINEMA RC Server', nargs='?')
parser.add_argument(
    '-pass', '--password', help='User password of SINEMA RC Server', nargs='?')
parser.add_argument(
    '-dh', '--databasehost', help='Hostname of database', nargs='?', default='localhost')
parser.add_argument(
    '-db', '--database', help='Hostname of database', nargs='?', default='srcexample')
parser.add_argument(
    '-du', '--databaseuser', help='Username for database', nargs='?', default='user')
parser.add_argument(
    '-dp', '--databasepass', help='Passphrase for database', nargs='?', default='user')

args = parser.parse_args()
#1. Connect to RC server
src_client = src_api(args.addr, port=args.port, username=args.user, password=args.password)
db_client = psycopg2.connect('''dbname='{}' user='{}' host='{}' password='{}\''''.format(args.database,args.databaseuser,args.databasehost,args.databasepass))
    
# Create table in database, if it not exists
try:
    cur = db_client.cursor()
    cur.execute(SQL_CREATE_TABLE)
    db_client.commit()
    logging.info('SQL table checked')
except Exception as error:
    logging.error(error)
    # In case of exception cancel current transaction block
    db_client.cancel()
    db_client.rollback()
finally:
    if db_client and cur and not cur.closed:
        cur.close()



#Cyclic polling of user log
while(True):
    now_start = datetime.datetime.now()
    logging.debug('Request server')
    server_response = src_client.get_user_log()
    logging.debug('Server Request')
    logging.debug(datetime.datetime.now()-now_start)
    now_database = datetime.datetime.now()
    if server_response['status_code'] == STATUS_OK:
        data = server_response['data']
        json_db = []
        for datapoint in data:
            try:
                
                cur = db_client.cursor()
                try:
                    port = int(datapoint["destinationPort"])
                except ValueError:
                    port = -1

                # set current acitve conneciton to 0
                if '-' in datapoint["duration"]:
                    duration = 0
                else:
                    duration = float(datapoint["duration"])

                data_usage =  float(datapoint["packageCounter"].split(' ')[1].replace('(',''))
                data_usage_converter = 1
                if 'GB' in datapoint["packageCounter"]:
                    data_usage_converter = 1000000000
                elif 'MB' in datapoint["packageCounter"]:
                    data_usage_converter = 1000000
                elif 'KB' in datapoint["packageCounter"]:
                    data_usage_converter = 1000
                
                data_usage = int(data_usage * data_usage_converter)
                package_count= int(datapoint["packageCounter"].split(' ')[0])

                cur.execute(SQL_ADD_ENTRY, (
                    datapoint["id"],
                    datapoint["startTime"],
                    datapoint["username"],
                    datapoint["endpoint"],
                    port,
                    duration,
                    data_usage,
                    package_count
                ))
                db_client.commit()
            except Exception as error:
                logging.debug(error)
                # In case of exception cancel current transaction block
                db_client.cancel()
                db_client.rollback()
            finally:
                if db_client and cur and not cur.closed:
                    cur.close()

        logging.debug('DB push')
        logging.debug(datetime.datetime.now()-now_database)
        logging.debug('Complete request')
        logging.debug(datetime.datetime.now()-now_start)
        logging.info('Polled successfully')
        sleep(600)


