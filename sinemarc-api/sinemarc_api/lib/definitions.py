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

# Introduced with V3.2
GET_SHOW_TICKET_NUMBER_STATUS = '/system/license/showticketnumbers'
UPDATE_SHOW_TICKET_NUMBER_STATUS = '/system/license/showticketnumbers'
RESET_LICENSE_CONTAINER = '/system/license/reset_license_system'
REACTIVATE_LICENSE = 'system/license/retry_activate'
MANAGE_LICENSES = 'system/license/manage'
GET_USER_CLIENT_LICENSE_LIST = 'system/license/clients'
GET_USER_CLIENT_LICENSE_DETAILS = 'system/license/clients/{}'
DELETE_USER_CLIENT_LICENSE_FROM_LIST = '/system/license/clients/{}'
GET_FLOATING_LIST = '/system/license/clients/floating'
ASSIGN_TO_STANDARD_LICENSE = '/system/license/clients/floating/{}'
GET_USER_CLIENT_FLOATING_DETAILS = '"/system/license/clients/floating/{}'
GET_HISTORY_LIST = '/system/license/clients/floating/history'
ASSIGN_TO_STANDARD_LICENSE = '/system/license/clients/floating/history/{}'
GET_USER_CLIENT_HISTORY_DETAILS = '/system/license/clients/floating/history/{}'
GET_EDGE_CLIENT_LICENSE_LIST = '/system/license/edgeclients'
GET_EDGE_CLIENT_LICENSE_DETAILS = '/system/license/edgeclients/{}'
DELETE_EDGE_CLIENT_LICENSE_FROM_LIST = '/system/license/edgeclients/{}'
GET_DEVICE_LICENSE_LIST = '/system/license/devices'
GET_DEVICE_LICENSE_DETAILS = '/system/license/devices/{}'
DELETE_DEVICE_LICENSE_FROM_LIST = '/system/license/devices/{}'
ACTIVATE_BACKUP_RESTORE = '/system/backup/{}'
GET_RESTORE_STATUS = '/system/backup/{}/status'
GET_THE_VALUES_OF_THE_PASSWORD_POLICY_SETTINGS= '/security/general/passwordpolicy' 
CHANGE_PASSWORD_POLICY_SETTINGS= '/security/general/passwordpolicy' 
GET_THE_VALUES_OF_THE_BRUTE_FORCE_SETTINGS= '/security/general/bruteforceprevention' 
CHANGE_BRUTE_FORCE_SETTINGS= '/security/general/bruteforceprevention' 
RENEW_FALLBACK_CERTIFICATE= '/security/certificates/fallback' 
GET_FALLBACK_CERTIFICATE_DETAILS= '/security/certificates/fallback' 
IMPORT_UMC_CA= '/security/umc/ca' 
DELETE_UMC_CA= '/security/umc/ca/<ID>'	 
GET_ALL_UMC_CA= '/security/umc/ca' 
GET_DETAILS_OF_UMC_CA_CERTIFICATE= '/security/umc/ca/<ID>'	 
IMPORT_UMC_CERTIFICATE= '/security/umc/certificate' 
DELETE_UMC_CERTIFICATE= '/security/umc/certificate/<ID>'	 
GET_ALL_UMC_CERTIFICATES= '/security/umc/certificate' 
EDIT_UPLOAD_SERVER_SETTINGS= '/services/uploadsettings' 
GET_SNMP_SETTINGS= '/services/snmpsettings' 
REMOVE_SNMP_SETTINGS= '/services/snmpsettings' 
EDIT_USER= '/accounts/users/<ID>'	 
GET_USER= '/accounts/users/<ID>'	 
EDIT_ROLE= '/accounts/roles/<ID>'	 
GET_VXLAN_DEVICES= '/vxlan/devices' 
GET_VXLAN_DEVICE= '/vxlan/devices/<ID>'	 
START_DCP_DISCOVERY_FOR_THE_DEVICE= '/vxlan/devices' 
GET_ALLOWED_COMMUNICATION_NODES_OF_THE_DEVICE= '/vxlan/devices/communicationnodes?deviceId={integer}'	 
DELETE_ALLOWED_NODE_OF_THE_DEVICE= '/vxlan/devices/communicationnodes' 
GET_ALL_DISCOVERED_NODES_OF_THE_DEVICE= '/vxlan/devices/foundnodes?deviceId={integer}'	 
ADD_MANUAL_NODE_TO_ALLOWED_COMMUNICATION_TABLE= '/vxlan/devices/foundnodes' 
GET_VXLAN_SETTINGS= '/vxlan/settings' 
SET_VXLAN_SETTINGS= '/vxlan/settings' 
EDIT_VXLAN_SETTINGS= '/vxlan/settings' 
GET_VXLAN_BRIDGES= '/vxlan/layer_networks' 
GET_VXLAN_BRIDGE_DETAILS= '/vxlan/layer_networks/<ID>'	 
ADD_VXLAN_BRIDGE= '/vxlan/layer_networks' 
DELETE_VXLAN_BRIDGE= '/vxlan/layer_networks/<ID>'	 
EDIT_GROUP= '/connections/groups/<ID>'	 
EDIT_NODE_OF_THE_LOCAL_CONNECTIONS_SUBNET_NODE= '/localconnections/connections/subnets/nodes/<ID>'	 
ADD_DEVICE_ACCESS_GROUP_TO_DEVICE= '/connections/devices/deviceaccess/groups' 
REMOVE_DEVICE_ACCESS_GROUP_OF_DEVICE= '/connections/devices/deviceaccess/groups' 
EDIT_SUBNET_OF_THE_DEVICE= '/connections/devices/subnets/<ID>'	 
ADD_PORT_GROUP_TO_SUBNET= '/connections/devices/subnets/portgroups' 
GET_ALL_PORT_GROUPS_OF_A_SUBNET= '/connections/devices/subnets/portgroups?subnetId={integer_value}'	 
GET_PORT_GROUP_OF_A_SUBNET= '/connections/devices/subnets/portgroups/<ID>'	 
EDIT_PORT_GROUP_NAME= '/connections/devices/subnets/portgroups/<ID>'	 
REMOVE_PORT_GROUP_FROM_SUBNET= '/connections/devices/subnets/portgroups/<ID>'	 
ADD_PORT_TO_PORT_GROUP_OF_SUBNET= '/connections/devices/subnets/portgroups/ports' 
REMOVE_PORT_FROM_PORT_GROUP_OF_SUBNET= '/connections/devices/subnets/portgroups/ports' 
GET_ALL_PARTICIPANT_GROUPS_OF_PORT_GROUP= '/connections/devices/subnets/portgroups/groups?portgroupId={integer_value}'	 
ADD_PARTICIPANT_GROUPS_TO_PORT_GROUP_OF_SUBNET= '/connections/devices/subnets/portgroups/groups' 
REMOVE_PARTICIPANT_GROUP_FROM_PORT_GROUP_OF_SUBNET= '/connections/devices/subnets/portgroups/groups' 
EDIT_NODE_OF_THE_SUBNET= '/connections/devices/subnets/nodes/<ID>'	 
ADD_PORT_GROUP_TO_NODE= '/connections/devices/subnets/nodes/portgroups' 
GET_ALL_PORT_GROUPS_OF_A_NODE= '/connections/devices/subnets/nodes/portgroups?nodeId={integer_value}'	 
GET_PORT_GROUP_OF_A_NODE= '/connections/devices/subnets/nodes/portgroups/<ID>'	 
EDIT_PORT_GROUP_NAME= '/connections/devices/subnets/nodes/portgroups/<ID>'	 
REMOVE_PORT_GROUP_FROM_NODE= '/connections/devices/subnets/nodes/portgroups/<ID>'	 
ADD_PORT_TO_PORT_GROUP_OF_NODE= '/connections/devices/subnets/nodes/portgroups/ports' 
REMOVE_PORT_FROM_PORT_GROUP_OF_NODE= '/connections/devices/subnets/nodes/portgroups/ports' 
GET_ALL_PARTICIPANT_GROUPS_OF_PORT_GROUP= '/connections/devices/subnets/nodes/portgroups/groups?portgroupId={integer_value}'	 
ADD_PARTICIPANT_GROUPS_TO_PORT_GROUP_OF_NODE= '/connections/devices/subnets/nodes/portgroups/groups' 
REMOVE_PARTICIPANT_GROUP_FROM_PORT_GROUP_OF_NODE= '/connections/devices/subnets/nodes/portgroups/groups' 
EDIT_DEVICE= '/connections/devices/<ID>'	 
GET_DEVICE= '/connections/devices/<ID>'	 
GET_SERVER_OVERVIEW= '/system/overview'
GET_DNS_SETTINGS= '/system/network/dns' 
SET_WEBSERVER_CONFIGURATION= '/system/network/webserver' 
EDIT_VIRTUAL_SUBNET_ADDRESS_SPACE_SETTINGS= '/system/vpnaddressspace/virtualsubnetsettings' 
EDIT_OPENVPN_ADDRESS_SPACE_SETTINGS= '/system/vpnaddressspace/openvpn' 
EDIT_OPENVPN_ADDRESS_SPACE_SETTINGS= '/system/vpnaddressspace
EDIT_SMS_GATEWAY_PROVIDER= '/system/smsandemail/sms/<ID>'	 
GET_A_TOKEN_TO_RESET_FACTORY_SETTINGS= '/system/timebasedsystemtoken' 
RESETTING_THE_SYSTEM_TO_FACTORY_SETTINGS_USING_A_SUPER_ADMIN_PASSWORD = '/system/settings/factoryreset' 











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

LoginType_Mapping = {

    'password' : 1,
    'pki' : 2
}