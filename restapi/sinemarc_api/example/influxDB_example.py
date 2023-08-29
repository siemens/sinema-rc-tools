#!/usr/bin/python3
# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

# pylint: disable=line-too-long, c-extension-no-member, global-statement, broad-except

"""

Name:
    influxDB_example.py

Description:
    Example to push user log in to in influxDB


Author:
    Siemens Support

Copyright:
    Copyright (c) 2022 SIEMENS AG

"""

from time import sleep
from influxdb import InfluxDBClient
from sinemarc_api.lib.srcapi_core import src_api
from sinemarc_api.lib.definitions import STATUS_OK
import argparse



#Example
# This will push userlog to an influx DB
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

args = parser.parse_args()
#1. Connect to RC server
src_client = src_api(args.addr, port=args.port, username=args.user, password=args.password)
db_client = InfluxDBClient(host=args.databasehost, port=8086)
    
databases = db_client.get_list_database()
database_exists = False
for database in databases:
    if database['name'] == args.database:
        database_exists = True
        break

# Generate Database if it not already exists
if not database_exists:
    db_client.create_database(args.database)
    print('Create database as it not exists')
else:
    db_client.switch_database(args.database)
    print('Switch database as it already exists')



last_polled_id = 0
#Cyclic polling of user log
while(True):
    server_response = src_client.get_user_log()
    current_max_id = last_polled_id
    if server_response['status_code'] == STATUS_OK:
        data = server_response['data']
        json_db = []
        for datapoint in data:
            if datapoint['id'] > last_polled_id:
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

                json_db.append(
                    {
                        "measurement": "srcUserEvent",
                        "tags": {
                            "user": datapoint["username"],
                            "id": datapoint["id"],
                            "endpoint": datapoint["endpoint"],
                            "destinationPort": datapoint["destinationPort"],
                        },
                        "time": datapoint["startTime"],
                        "fields": {
                            "duration": duration,
                            "usage": data_usage,
                            "packages": package_count
                        }

                    })
                if datapoint['id']>current_max_id:
                    current_max_id = datapoint['id']
        last_polled_id = current_max_id

        if json_db:
            db_client.write_points(json_db)
            print('Polled successfully and added new datapoints')
        else:
            print('Polled successfully and added no new datapoints')
        sleep(10)


