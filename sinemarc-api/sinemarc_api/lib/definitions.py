#!/usr/bin/python3
# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

# pylint: disable=line-too-long, c-extension-no-member, global-statement, broad-except

"""

Name:
    definitions.py

Description:
    definitions.py contains constant definitions of various parameters
    --> e.g. path definitions, file names, etc.


Author:
    Siemens Support

Copyright:
    Copyright (c) 2022 SIEMENS AG

"""

STATUS_ACCEPTED = 202
STATUS_OK = 200
STATUS_FORBIDDEN = 403
STATUS_UNAUTHORIZED = 401
STATUS_NOT_FOUND = 404
STATUS_CONFLICT = 409
STATUS_METHOD_NOT_ALLOWED = 405
STATUS_UNPROCESSABLE_ENTRY = 422

TOKEN_PATH='/api-auth'
TOKEN_JSON_KEY = 'token'

GET_DNS = '/system/network/dns'
SET_DNS = '/system/network/dns'


GET_LICENSE_INFO = '/system/license'
ACTIVATE_LICENSE = '/system/license/activate'


INIT_SERVER = '/system/init'


GET_API_SETTINGS = '/services/apisettings'
SET_API_SETTINGS = '/services/apisettings'

GET_SYSTEM_OVERVIEW = '/system/overview'
GET_SYSTEM_LOAD = '/system/overview/load'

GET_NETWORK_SETTINGS = '/system/network?interface={}'
SET_NETWORK_INTERFACE = '/system/network'

GET_WEBSERVER_SETTINGS = '/system/network/webserver'
SET_WEBSERVER_SETTINGS = '/system/network/webserver'

SEND_PING = '/system/network/ping'

GET_STATIC_ROUTES = '/system/network/staticroutes'
SET_STATIC_ROUTES = '/system/network/staticRoutes'
DELETE_STATIC_ROUTES = '/system/network/staticroutes/{}'

GET_NTP_CONFIGURATION = '/system/dateandtime/ntp'
SET_NTP_CONFIGURATION = '/system/dateandtime/ntp'
DEACTIVATE_NTP_CONFIGURATION = '/system/dateandtime/ntp'

GET_DEVICES = '/connections/devices'
GET_DEVICE_STATUS = '/connections/devices/status/{}'
GET_DEVICE_OPENVPN_ID = '/connections/devices/connectionparameter?deviceId={}'
GET_DEVICE_OPENVPN_CONFIG = '/connections/devices/connectionparameter/{}'
GET_DEVICE_PARTICIPANT_ID = '/connections/devices/groups?deviceId={}'
GET_DEVICE_SUBNET_ID = '/connections/devices/subnets?deviceId={}'
GET_DEVICE_SUBNET_CONFIG = '/connections/devices/subnets/{}'
GET_DEVICE_SUBNET_GROUPS = '/connections/devices/subnets/groups?subnetId={}'
GET_DEVICE_SUBNET_DEVICES = '/connections/devices/subnets/nodes?subnetId={}'
GET_DEVICE_SUBNET_DEVICES_DETAILS = '/connections/devices/subnets/nodes/{}'
GET_DEVICE_SUBNET_DEVICE_GROUP = '/connections/devices/subnets/nodes/groups?nodeId={}'
SET_DEVICE_STATUS = '/connections/devices/status/{}'
DELETE_DEVICE ='/connections/devices/{}'
CREATE_DEVICE = '/connections/devices'
CREATE_OPENVPN = '/connections/devices/connectionparameter'
DELETE_OPENVPN = '/connections/devices/connectionparameter/{}'
ASSIGN_DEVICE_GROUP = '/connections/devices/groups'
REMOVE_DEVICE_GROUP = '/connections/devices/groups'
CREATE_SUBNET = '/connections/devices/subnets'
DELETE_SUBNET = '/connections/devices/subnets/{}'
ASSIGN_SUBNET_GROUP= '/connections/devices/subnets/groups'
DELETE_SUBNET_GROUP='/connections/devices/subnets/groups'
ASSING_SUBNET_NODE = '/connections/devices/subnets/nodes'
DELETE_SUBNET_NODE = '/connections/devices/subnets/{}'
ASSIGN_SUBNET_NODE_GROUP = '/connections/devices/subnets/nodes/groups'
DELETE_SUBNET_NODE_GROUP = '/connections/devices/subnets/nodes/groups'

GET_GROUPS='/connections/groups'
CREATE_GROUP = '/connections/groups'
DELETE_GROUP = '/connections/groups/{}'
ASSIGN_GROUPS_RELATION = '/connections/groups/destination/{}'
DELETE_GROUPS_RELATION = '/connections/groups/destination/{}'
GET_GROUP_RELATION = '/connections/groups/destination/{}'

GET_CURRENT_WEBSERVER = '/security/certificates/webserver'

GET_CLIENT_LICENSE = '/accounts/clients'
DELETE_CLIENT_LICENSE = '/accounts/clients/{}'
GET_CLIENT_LICENSE_DETAILS = '/accounts/clients/{}'

GET_ROLES = '/accounts/roles'
CREATE_ROLES = '/accounts/roles'
GET_ROLE_DETAIL = '/accounts/roles/{}'
DELETE_ROLE = '/accounts/roles/{}'

GET_USERS = '/accounts/users'
GET_USER_ACTIVATION_STATUS ='/accounts/users/status/{}'
SET_USER_ACTIVATION_STATUS ='/accounts/users/status/{}'
GET_USER_DETAIL = '/accounts/users/{}'
GET_USER_GROUPS = '/accounts/users/groups?userId={}'
GET_USER_ROLES = '/accounts/users/roles?userId={}'
DELETE_USER = '/accounts/users/{}'
CREATE_USER = '/accounts/users'
ASSIGN_USER_GROUP = '/accounts/users/groups'
DELETE_USER_GROUP = '/accounts/users/groups'
ASSIGN_USER_ROLE = '/accounts/users/roles'
DELETE_USER_ROLE = '/accounts/users/roles'


GET_USER_AGREEMENT = '/accounts/useragreement'
SET_USER_AGREEMENT = '/accounts/useragreement'

GET_USER_LOG = '/system/userlog/entries'

SET_WEBSERVER_CERT = '/security/certificates/webserver'

CLI_COMMANDS = '''!
sinemarc
shutdown
port {}
device id {}
device pw {}
addr {}
verification fingerprint {}
no shutdown
!'''

Device_typ_mapping= {
    'other':0,
    'S615': 1,
    'M800':2,
    'SC600': 3,
    'CP1243-1':4,
    'CP1243-7':5,
    'RTU303xC':6,
    'RTU3010C':7,
}

Connection_typ_mapping = {
    'permanent':1,
'digital_input':2,
'wake_up_sms':-1,
'digital_input_wake_up_sms':5
}

