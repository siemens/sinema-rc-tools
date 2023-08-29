"""

Name:
    srcapi_core.py

Description:


Author:
    Siemens Support

Copyright:
    Copyright (c) 2022 SIEMENS AG

"""

# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

import logging
import requests

from sinemarc_api.lib.definitions import *
from sinemarc_api.lib.exception_definition import *


class src_api:

    def __init__(self, address, port=443, username='admin', password='admin', timeout=500, verify_certificate=False):
        """Create new object for communication to SINEMA RC Server. API License is needed

        Args:
            address (String): IP-Address or DNS name of the Server
            port (int, optional): Webserver Port. Defaults to 443.
            username (str, optional): User login name. Defaults to 'admin'.
            password (str, optional): User password. Defaults to 'admin'.
            timeout (int, optional): Wait timeout for communication. Defaults to 500.
            verify_certificate (bool, optional): Should SINEMA RC Webserver certificate be checked. Defaults to False.
        """
        self.address = address
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout
        self.verify_certificate = verify_certificate
        if not verify_certificate:
            requests.packages.urllib3.disable_warnings()
        self.__token = None
        self.__session = requests.session()
        self.base_uri = 'https://{}:{}/api/v1'.format(self.address, self.port)
        self.__get_token()
        self.dns = None
        self.wan_address = None
        self.internal_address = None
        self.sha256 = None
        self.sha1 = None
        if self.__token:
            self.__update_system_info(self.get_current_webserver())

    def __update_system_info(self, webserver):
        """Set basic information of webserver, which is needed to connect a device

        Args:
            webserver (Json): Return result of get_current_webserver()
        """
        try:
            if webserver['status_code'] == STATUS_OK:
                webserver_data = webserver['data']
                if webserver_data.__contains__('alternateDns'):
                    self.dns = webserver_data['alternateDns']
                if webserver_data.__contains__('alternateIp1'):
                    self.wan_address = webserver_data['alternateIp1']
                if webserver_data.__contains__('alternateIp2'):
                    self.internal_address = webserver_data['alternateIp2']

                if webserver_data.__contains__('sha256'):
                    self.sha256 = webserver_data['sha256']
                if webserver_data.__contains__('sha1'):
                    self.sha1 = webserver_data['sha1']

        except Exception:
            pass

    def set_DNS_server(self, hostname, externallyResolvable=None, dnsPrimary=None, dnsSecondary=None):
        """Configure DNS Server on SINEMA RC Server

        Args:
            hostname (String): DNS Name of the SINEMA RC Server
            externallyResolvable (Boolean, optional): Is the hostname a resolvable DNS name. Defaults to None.
            dnsPrimary (String, optional): IP-Address of main DNS Server. Defaults to None.
            dnsSecondary (String, optional): IP-Address of Backup DNS Server. Defaults to None.

        Returns:
            Json: Result of request
        """
        json_data = {'hostname': hostname}
        if externallyResolvable:
            json_data['externallyResolvable'] = externallyResolvable
        if dnsPrimary:
            json_data['dnsPrimary'] = dnsPrimary
        if externallyResolvable is not None:
            json_data['dnsSecondary'] = dnsSecondary

        return self.__post(SET_DNS, json_data)

    def get_DNS_server(self):
        """Get current DNS Configuration

        Returns:
            Json: current DNS Configuration
        """
        return self.__get(GET_NETWORK_SETTINGS)

    def activate_license(self, ticketNo, amount=None):
        """Activate a new license on your SINEMA RC server

        Args:
            ticketNo (String): Ticket ID which is provided on the certificate of license
            amount (Integer, optional): Number of nodes of a user license, which should be activated. Defaults to None.

        Returns:
            Json: Result of activation
        """
        json_data = {'ticketNo': ticketNo}
        ticket_validation = self.__post(GET_LICENSE_INFO, json_data)
        if amount:
            json_data['amount'] = amount

        if ticket_validation.__contains__('Accepted'):
            return self.__post(ACTIVATE_LICENSE, json_data)
        else:
            return ticket_validation

    def get_license_information(self):
        """Get information of current active licenses

        Returns:
            Json: License information
        """
        license_ids = self.__get(GET_LICENSE_INFO)
        if license_ids['status_code'] == STATUS_OK:
            license_details = []
            for license in license_ids['data']:
                detail_temp = self.__get(
                    '{}/{}'.format(GET_LICENSE_INFO, license['id']))['data']
                detail_temp['id'] = license['id']
                license_details.append(detail_temp)
            return {'license_ids': license_ids['data'], 'license_details': license_details, 'status_code': license_ids['status_code']}
        else:
            return license_ids

    def release_license(self, ticketNo):
        """Release license from server

        Args:
            ticketNo (String): Ticket ID which is provided on the certificate of license

        Returns:
            Json: Result of release
        """
        return self.__delete('{}/{}'.format(GET_LICENSE_INFO, ticketNo))

    def server_init(self, superAdmin, superAdminPw):
        """Set server after installation, this can only be used if no one was over locked on

        Args:
            superAdmin (String): User is in default admin
            superAdminPw (String): Password is in default admin

        Returns:
            Json: Result of init
        """
        json_data = {'superAdmin': superAdmin, 'superAdminPw': superAdminPw}
        return self.__post(INIT_SERVER, json_data)

    def get_server_api_settings(self):
        """Get current api settings

        Returns:
            Json: Current API settings
        """
        return self.__get(GET_API_SETTINGS)

    def set_server_api_settings(self, active=True, startTrial=None, tokenExpireTime=None):
        """Configure api settings

        Args:
            active (bool, optional): Activate or deactivate the server. Defaults to True.
            startTrial (bool, optional): Start the 14 days trial phase. Defaults to None.
            tokenExpireTime (Integer, optional): Number of days in which the authentication token is valid. Defaults to None.

        Returns:
            Json: Result of configuration
        """
        json_data = {'active': active}
        if startTrial is not None:
            json_data['startTrial'] = startTrial
        if tokenExpireTime:
            json_data['tokenExpireTime'] = tokenExpireTime

        return self.__post(SET_API_SETTINGS, json_data)

    def get_server_status(self):
        """Get basic information about the server status

        Returns:
            Json: Information about the overview and current load of the server
        """
        return {'overview': self.__get(GET_SYSTEM_OVERVIEW), 'load': self.__get(GET_SYSTEM_LOAD)}

    def get_network_interface_status(self, interface_id=0):
        """Get information about network configuration

        Args:
            interface_id (int, optional): The network interface which should be retrieved 0 = WAN / 1 = LAN1 / 2 = LAN2 / 3 = LAN3 / 4 = LAN4. Defaults to 0.

        Raises:
            src_wrong_datatype: Error if interface_id is wrongly used

        Returns:
            Json: Current network status
        """
        if isinstance(interface_id, int):
            return self.__get(GET_NETWORK_SETTINGS.format(interface_id))
        else:
            raise src_wrong_datatype('interface_id has to be integer')

    def set_network_interface(self, interface_id, dhcp=None, ipAddress=None, networkMask=None, gateway=None, MTU=None, wanIp=None,
                              ipv6Enabled=None, ipv6Slaac=None, ipv6Address=None, ipv6PrefixLength=None, ipv6Gateway=None, masquerading=None):
        """Configure a network interface

        Args:
            interface_id (integer, optional): The network interface which should be retrieved 0 = WAN / 1 = LAN1 / 2 = LAN2 / 3 = LAN3 / 4 = LAN4. Defaults to 0.
            dhcp (Bool, optional): Should DHCP be used to configure the network interface. Defaults to None.
            ipAddress (String optional): Static IPv4-Address. Defaults to None.
            networkMask (String, optional): Static IPv4-Subnet Mask. Defaults to None.
            gateway (String, optional): Static IPv4-Address for default gateway. Defaults to None.
            MTU (Integer, optional): MTU size. Defaults to None.
            wanIp (String, optional): External IPv4-Address of NAT router. Defaults to None.
            ipv6Enabled (Bool, optional): Should IPv6 enabled. Defaults to None.
            ipv6Slaac (Bool, optional): Should IPv6 be configured via Claac. Defaults to None.
            ipv6Address (String, optional): Static IPv6-Address. Defaults to None.
            ipv6PrefixLength (String, optional): Static IPv6-Prefix Length. Defaults to None.
            ipv6Gateway (String, optional): Static IPv6-Address for default gateway. Defaults to None.
            masquerading (Bool, optional): Should every packet, which is send be the interface, be source natted. Defaults to None.

        Raises:
            src_wrong_datatype: Error if interface_id is wrongly used
            src_missing_value: If there are errors for Slaac vs Static IPv6 configuration


        Returns:
            Json: Result of network configuration
        """

        if not isinstance(interface_id, int):
            raise src_wrong_datatype('interface has to be integer')

        json_data = {'interface': interface_id}

        if not (ipAddress and networkMask and gateway) and not ipv6Enabled and not dhcp:
            raise src_missing_value(
                'As DHCP and ipv6 is disabled, an IP-Address, Network Mask and gateway is needed')

        if ipv6Enabled and not ipv6Slaac and not (ipv6Address and ipv6PrefixLength and not ipv6Gateway):
            raise src_missing_value(
                'As IPv6 is enabled and SLAAC is disabled, an IP-Address, Network Mask and gateway is needed')

        if dhcp is not None:
            json_data['dhcp'] = dhcp
        if ipAddress:
            json_data['ipAddress'] = ipAddress
        if networkMask:
            json_data['networkMask'] = networkMask
        if gateway:
            json_data['gateway'] = gateway
        if MTU:
            json_data['MTU'] = MTU
        if wanIp:
            json_data['wanIp'] = wanIp
        if ipv6Enabled is not None:
            json_data['ipv6Enabled'] = ipv6Enabled
        if ipv6Slaac:
            json_data['ipv6Slaac'] = ipv6Slaac
        if ipv6Address:
            json_data['ipv6Address'] = ipv6Address
        if ipv6PrefixLength:
            json_data['ipv6PrefixLength'] = ipv6PrefixLength
        if ipv6Gateway:
            json_data['ipv6Gateway'] = ipv6Gateway
        if masquerading:
            json_data['ipAddress'] = masquerading

        return self.__post(SET_NETWORK_INTERFACE, json_data)

    def get_webserver_configuration(self):
        """Get current webserver port configuration

        Returns:
            Json: Current webserver configuration
        """
        return self.__get(GET_WEBSERVER_SETTINGS)

    def set_webserver_configuration(self, httpsPort, fallBackPort=None):
        """Configure webserver ports

        Args:
            httpsPort (Integer): Configure main port for website
            fallBackPort (Integer, optional): Configure fallback port for device fallback of the webserver. Defaults to None.

        Returns:
            Json: Result of configuration
        """
        json_data = {'httpsPort': httpsPort}
        if fallBackPort:
            json_data['fallBackPort'] = fallBackPort

        return self.__post(SET_NETWORK_INTERFACE, json_data)

    def send_ping(self, Address, repeat=None, timeout=None):
        """Send ping from server to an address

        Args:
            Address (String): IP-Address or DNS name of target dervice
            repeat (Integer, optional): How often the ping should be send. Defaults to None.
            timeout (Integer, optional): How long the server should wait for a reply. Defaults to None.

        Returns:
            Json: output if the ping was successful
        """
        json_data = {'address': Address}

        if repeat:
            json_data['repeat'] = repeat
        if timeout:
            json_data['timeout'] = timeout

        return self.__post(SEND_PING, json_data)

    def get_static_routes(self):
        """
        Get static route of the server

        Returns:
            Json: Current configured static routes
        """
        static_route_ids = self.__get(GET_STATIC_ROUTES)
        if static_route_ids['status_code'] == STATUS_OK:
            route_details = []
            route_status = []
            for route in static_route_ids['data']:
                detail_temp = self.__get(
                    '{}/{}'.format(GET_STATIC_ROUTES, route['id']))['data']
                detail_temp['id'] = route['id']
                route_details.append(detail_temp)
                status_temp = self.__get(
                    '{}/{}/status'.format(GET_STATIC_ROUTES, route['id']))['data']
                status_temp['id'] = route['id']
                route_status.append(status_temp)
            return {'route_ids': static_route_ids['data'], 'route_details': route_details, 'route_status': route_status, 'status_code': static_route_ids['status_code']}
        else:
            return static_route_ids

    def create_static_route(self, destinationNetwork, networkMask, gateway, interface):
        """
        Create a new static route

        Args:
            destinationNetwork (String): IPv4-Address of destination network
            networkMask (String): IPv4-Subnetmask for destination network
            gateway (String): IPv4-Address of gateway
            interface (Integer): The network interface which should be retrieved 0 = WAN / 1 = LAN1 / 2 = LAN2 / 3 = LAN3 / 4 = LAN4. Defaults to 0.

        Returns:
            Json: Result of configuration
        """
        json_data = {'destinationNetwork': destinationNetwork,
            'networkMask': networkMask, 'gateway': gateway, 'interface': interface}
        return self.__post(SET_STATIC_ROUTES, json_data)

    def delete_static_route(self, id):
        return self.__delete(DELETE_STATIC_ROUTES.format(id))

    def get_ntp_configuration(self):
        return self.__get(GET_NTP_CONFIGURATION)

    def set_ntp_configuration(self, active, primaryNtp=None, secondNtp=None, timezone=None):
        if active:
            if not primaryNtp:
                raise src_missing_value('Missing value for primary DNS')
            if not timezone:
                raise src_missing_value('Missing value for timezone')

            json_data = {'primaryNtp': primaryNtp, 'timezone': timezone}
            if secondNtp:
                json_data['secondNtp'] = secondNtp

            return self.__post(SET_NTP_CONFIGURATION, json_data)
        else:
            return self.__delete(DEACTIVATE_NTP_CONFIGURATION)

    def get_devices(self, device_id=None, search=None):
        """
        Get current devices, which are configured

        Args:
            device_id (Integer, optional): Device id to get details for this device. Defaults to None.
            search (String, optional): Search string to filter for specific devices. Defaults to None.

        Raises:
            src_wrong_usage: device_id and search string can't be used at the same time

        Returns:
            Json: With Details about all devices, which were requested
        """
        if device_id and search:
            raise src_wrong_usage(
                'Device_id and search can not be used at the same time')
        if device_id:
            return self.__get_device_details(device_id)
        else:
            if search:
                device_ids = self.__get(
                    '{}?search={}'.format(GET_DEVICES, search))
            else:
                device_ids = self.__get(GET_DEVICES)
            if device_ids['status_code'] == STATUS_OK:
                device_details = []
                for device in device_ids['data']:
                    device_details.append(
                        self.__get_device_details(device['id']))
                return {'device_ids': device_ids['data'], 'device_details': device_details, 'status_code': device_ids['status_code']}
            else:
                return device_ids

    def __get_device_details(self, id):
        """
        Retrieve details for a specific device

        Args:
            id (Integer): device id

        Returns:
            Json: With current details about devices
        """
        device_temp = self.__get('{}/{}'.format(GET_DEVICES, id))['data']
        device_temp['id'] = id
        #Get current status
        device_temp['status'] = self.__get(GET_DEVICE_STATUS.format(id))[
            'data']['status']
        #Get OPENVPN configuration
        openvpn_ids = self.__get(GET_DEVICE_OPENVPN_ID.format(id))['data']
        openvpn_details = []
        if openvpn_ids:
            for openvpn_id in openvpn_ids:
                temp_openvpn = self.__get(
                    GET_DEVICE_OPENVPN_CONFIG.format(openvpn_id['id']))['data']
                temp_openvpn['id'] = openvpn_id['id']
                openvpn_details.append(temp_openvpn)
            device_temp['openvpn_details'] = openvpn_details
        #Get participant group configuration
        participant_group_ids = self.__get(
            GET_DEVICE_PARTICIPANT_ID.format(id))['data']
        if participant_group_ids:
            device_temp['participant_group'] = participant_group_ids
        #Get subnet configuration
        subnet_ids = self.__get(GET_DEVICE_SUBNET_ID.format(id))['data']
        subnet_details = []
        if subnet_ids:
            for subnet_id in subnet_ids:
                temp_subnet = self.__get(
                    GET_DEVICE_SUBNET_CONFIG.format(subnet_id['id']))['data']
                temp_subnet['id'] = subnet_id['id']
                temp_subnet['group_ids'] = self.__get(
                    GET_DEVICE_SUBNET_GROUPS.format(subnet_id['id']))['data']
                temp_subnet_node_ids = self.__get(
                    GET_DEVICE_SUBNET_DEVICES.format(subnet_id['id']))['data']
                temp_subnet_nodes = []
                for temp_subnet_node_id in temp_subnet_node_ids:
                    temp_subnet_node = self.__get(
                        GET_DEVICE_SUBNET_DEVICES_DETAILS.format(temp_subnet_node_id['id']))['data']
                    temp_subnet_node['id'] = temp_subnet_node_id['id']
                    temp_subnet_node['group_ids'] = self.__get(
                        GET_DEVICE_SUBNET_DEVICE_GROUP.format(temp_subnet_node_id['id']))['data']
                    temp_subnet_nodes.append(temp_subnet_node)
                if temp_subnet_nodes:
                    temp_subnet['nodes'] = temp_subnet_nodes
                subnet_details.append(temp_subnet)
            device_temp['subnet_details'] = subnet_details

        return device_temp

    def set_device_status(self, id, status):
        """
        Enable or disable a device

        Args:
            id (Integer): Device_id which should be enabled/disabled
            status (Bool): Enabled/Disabled

        Returns:
            Json: Result of configuration
        """
        json_data = {'status': status}
        return self.__put(SET_DEVICE_STATUS.format(id), json_data)

    def delete_device(self, id):
        """
        Delete a device

        Args:
            id (Integer): Device_id which should be deleted

        Returns:
            Json: Result of deletion
        """
        return self.delete_device(DELETE_DEVICE.format(id))

    def create_device(self, name, password, type, connectionType, vendor=None, smsGatewayProvider=None, gsmNumber=None, senderId=None, location=None, comment=None, fixedVpnAddress=None, defaultGateway=None,
                      openvpn_parameter=None, groupId=None, subnet_parameter=None, get_running_cli=False):
        """
        Create a new vpn device

        Args:
            name (String): Name of the device
            password (String): Password which the device should use to logon
            type (String or Integer): Device type can be name of type or number from manual
            connectionType (String or Integer): How the connection should be established
            vendor (String, optional): Name of vendor. Defaults to None.
            smsGatewayProvider (String, optional): SMS gateway for wake-up SMS. Defaults to None.
            gsmNumber (String, optional): Phone number of the device. Defaults to None.
            senderId (String, optional): Authentication of SMS for RTU303xC. Defaults to None.
            location (String, optional): Location of the device. Defaults to None.
            comment (String, optional): Comment for the device. Defaults to None.
            fixedVpnAddress (String, optional): OpenVPN address for the device. Defaults to None.
            defaultGateway (Bool, optional): Is the device configured as default gateway within the machine. Defaults to None.
            openvpn_parameter (Json or List of Json, optional): OpenVPN Parameter which should be used by the device. Defaults to None.
            groupId (Integer or List of Integer, optional): All participant group ids, which should have access to the device. Defaults to None.
            subnet_parameter (Json or List of Integer, optional): Subnet configuration. Defaults to None.
            get_running_cli (bool, optional): Should a list of CLI commands be created to connect the device. Defaults to False.


        Returns:
            Json: With result of the creation
        """
        if isinstance(type, str) and not Device_typ_mapping.__contains__(type):
            raise src_wrong_usage(
                'Only supported types are other, S615, M800, SC600, CP1243-1, CP1243-7, RTU303xC, RTU3010C')
        elif isinstance(type, str):
            numeric_type = Device_typ_mapping[type]
        else:
            numeric_type = type

        if senderId and not (numeric_type == 6):
            raise src_wrong_usage('SenderId is only supported for RTU303xC')

        if isinstance(connectionType, str) and not Device_typ_mapping.__contains__(connectionType):
            raise src_wrong_usage(
                'Only supported connection types permanent,digital_input,wake_up_sms,digital_input_wake_up_sms')
        elif isinstance(connectionType, str):
            numeric_connection_type = Connection_typ_mapping[connectionType]
            if numeric_connection_type == -1:
                if numeric_type == 3:
                    numeric_connection_type = 3
                elif numeric_type == 4:
                    numeric_connection_type = 4
        else:
            numeric_connection_type = connectionType

        json_data = {'name': name, 'password': password,
            'type': numeric_type, 'connectionType': numeric_connection_type}
        if vendor:
            json_data['vendor'] = vendor
        if smsGatewayProvider:
            json_data['smsGatewayProvider'] = smsGatewayProvider
        if gsmNumber:
            json_data['gsmNumber'] = gsmNumber
        if senderId:
            json_data['senderId'] = senderId
        if location:
            json_data['location'] = location
        if comment:
            json_data['comment'] = comment
        if fixedVpnAddress:
            json_data['fixedVpnAddress'] = fixedVpnAddress
        if defaultGateway is None:
            json_data['defaultGateway'] = defaultGateway

        device_id = self.__post(CREATE_DEVICE, json_data)

        if device_id['status_code'] != STATUS_OK:
            raise src_wrong_usage('Server reports {} for create device: {}'.format(
                device_id['status_code'], device_id['data']['detail']))

        device_id = device_id['data']['id']

        if not device_id:
            raise src_missing_value('Device could not be created')
        if openvpn_parameter:
            try:
                if isinstance(openvpn_parameter, list):
                    for openvpn in openvpn_parameter:
                        self.set_device_openvpn(
                            device_id, openvpn['ipAddress'], openvpn['port'], openvpn['protocol'])
                else:
                    self.set_device_openvpn(
                        device_id, openvpn_parameter['ipAddress'], openvpn_parameter['port'], openvpn_parameter['protocol'])

            except KeyError:
                raise src_missing_value(
                    'Openvpn parameter has to contain ipAddress, port, protocol')

        if groupId:
            self.set_device_group(device_id, groupId)

        if subnet_parameter:
            try:
                if isinstance(subnet_parameter, list):
                    for subnet in subnet_parameter:
                        self.__assign_device_subnet(subnet, device_id)
                else:
                    self.__assign_device_subnet(subnet_parameter, device_id)
            except KeyError:
                raise src_missing_value(
                    'Network parameter needs name, ipAddress, subnetMask, natMode')

        if get_running_cli:
            return {'device_id': device_id, 'wan_address': self.wan_address, 'internal_address': self.internal_address, 'fingerprint_sha1': self.sha1, 'fingerprint_sha256': self.sha256, 'port': self.port, 'running_cli': self.get_cli_commands(device_id, password)}
        else:
            return {'device_id': device_id, 'wan_address': self.wan_address, 'internal_address': self.internal_address, 'fingerprint_sha1': self.sha1, 'fingerprint_sha256': self.sha256, 'port': self.port}

    def get_cli_commands(self, device_id, device_password):
        """
        Get CLI command for a device to connect it with SINEMA RC

        Args:
            device_id (Integer): Id of the device which was returned by create device
            device_password (String): Password for the device to logon

        Returns:
            String: CLI Commands for the device
        """

        return CLI_COMMANDS.format(self.port, device_id, device_password, self.wan_address, self.sha256)

    def __assign_device_subnet(self, subnet_parameter, device_id):
        """
        Assign a subnet to a device

        Args:
            subnet_parameter (Json): Json with subnet parameter
            device_id (Integer): Device id

        Raises:
            src_wrong_usage: Raise error if server doesn't allow this subnet
        """
        if subnet_parameter.__contains__('virtualIp'):
            subnet_id = self.create_device_subnet(
                device_id, subnet_parameter['name'], subnet_parameter['ipAddress'], subnet_parameter['subnetMask'], subnet_parameter['natMode'], subnet_parameter['virtualIp'])
        else:
            subnet_id = self.create_device_subnet(
                device_id, subnet_parameter['name'], subnet_parameter['ipAddress'], subnet_parameter['subnetMask'], subnet_parameter['natMode'])

        if subnet_id['status_code'] != STATUS_OK:
            raise src_wrong_usage('Server reports {} for create device subnet: {}'.format(
                subnet_id['status_code'], subnet_id['data']['detail']))
        subnet_id = subnet_id['data']['id']

        if subnet_parameter.__contains__('groupId'):
            self.set_subnet_group(device_id, subnet_id,
                                  subnet_parameter['groupId'])

        if subnet_parameter.__contains__('node'):
            self.__assign_subnet_node(subnet_id, subnet_parameter['node'])

    def __assign_subnet_node(self, subnet_id, node):
        """
        Assign node to a subnet

        Args:
            subnet_id (integer): subnet id
            node (json): Parameter for the node
        """
        try:
            if isinstance(node, list):
                for node_single in node:
                    node_id = self.set_subnet_node(
                        subnet_id, node_single['name'], node_single['ipAddress'])
                    if node_id['status_code'] != STATUS_OK:
                        raise src_wrong_usage('Server reports {} for create node for device: {}'.format(
                            node_id['status_code'], node_id['data']['detail']))
                    node_id = node_id['data']['id']

                    if node.__contains__('groupId'):
                        self.__assign_subnet_node_group(
                            node_id, node['groupId'])
            else:
                node_id = self.set_subnet_node(
                      subnet_id, node['name'], node['ipAddress'])
                if node_id['status_code'] != STATUS_OK:
                    raise src_wrong_usage('Server reports {} for create node for device: {}'.format(
                      node_id['status_code'], node_id['data']['detail']))
                node_id = node_id['data']['id']
                if node.__contains__('groupId'):
                    self.__assign_subnet_node_group(
                          node_id, node['groupId'])
        except KeyError:
            raise src_wrong_usage('For node is name and ip needed.')

    def __assign_subnet_node_group(self, node_id, group_id):
        """
        Assign group access to a node within a subnet

        Args:
            node_id (integer): Id of the node
            group_id (integer): Id of the group

        Returns:
            Json: Result of configuration
        """
        return self.set_subnet_node_group(node_id, group_id)

    def set_device_openvpn(self, deviceId, ipAddress, port, protocol):
        """
        Configure the static OpenVPN settings which should be used by the device, without this the configuration will be created automatically

        Args:
            deviceId (Integer): Id of the device
            ipAddress (String): IP Address of OpenVPN server
            port (Integer): Port of OpenVPN server
            protocol (String): Protocol which should be used TCP or UDP

        Returns:
            Json: Result of configuration
        """
        json_data = {'deviceId': deviceId, 'ipAddress': ipAddress, 'port':port, 'protocol':protocol}
        return self.__post(CREATE_OPENVPN, json_data)

    def delete_device_openvpn(self, id):
        """
        Delete static OpenVPN configuration of a device

        Args:
            id (Integer): Id of the openvpn paramater set

        Returns:
            Json: result of delete
        """
        return self.__delete(DELETE_OPENVPN.format(id))

    def set_device_group(self, deviceId, groupId):
        """
        Assign a device to a group

        Args:
            deviceId (Integer): Id of the device
            groupId (Integer): Id of the group

        Returns:
            Json: Result of configuration
        """
        return self.__post(ASSIGN_DEVICE_GROUP, {'deviceId': deviceId, 'groupId':groupId})

    def delete_device_group(self, deviceId, groupId):
        """
        Remove a device from a group

        Args:
            deviceId (Integer): Id of the device
            groupId (Integer): Id of the group

        Returns:
            Json: Result of delete
        """
        return self.__delete(REMOVE_DEVICE_GROUP, {'deviceId': deviceId, 'groupId':groupId})

    def create_device_subnet(self, deviceId, name, ipAddress, subnetMask, natMode, virtualIp=None):
        """
        Assign a subnet to a device

        Args:
            deviceId (integer): Id of the device
            name (string): Name of the subnet
            ipAddress (string): IPv4-Address of the subnet
            subnetMask (string): IPv4-Subnetmask of the subnet
            natMode (integer): NAT-Modus: 0 = none / 1 = 1:1 NAT
            virtualIp (string, optional): Virtual IPv4 for NAT. Defaults to None.

        Returns:
            Json: Result of configuration
        """
        json_data = {'deviceId': deviceId, 'name': name, 'ipAddress':ipAddress, 'subnetMask':subnetMask, 'natMode':natMode}
        if virtualIp:
            json_data['virtualIp'] = virtualIp
        return self.__post(CREATE_SUBNET, json_data)

    def delete_device_subnet(self, subnet_id):
        """
        Delete a subnet from a device

        Args:
            subnet_id (Integer): Id of the subnet

        Returns:
            Json: Result of delete
        """
        return self.__delete(DELETE_SUBNET.format(subnet_id))

    def set_subnet_group(self, deviceId, subnetId, groupId):
        """
        Assign a subnet to a group

        Args:
            deviceId (Integer): Id of the affected device
            subnetId (Integer): Id of the affected subnet
            groupId (Integer): Id of the whished group

        Returns:
            Json: Result
        """
        return self.__post(ASSIGN_SUBNET_GROUP, {'deviceId': deviceId, 'subnetId':subnetId, 'groupId':groupId})

    def delete_subnet_group(self, deviceId, subnetId, groupId):
        """
        Delete a subnet from a group

        Args:
            deviceId (Integer): Id of the affected device
            subnetId (Integer): Id of the affected subnet
            groupId (Integer): Id of the whished group

        Returns:
            Json: Result
        """
        return self.__delete(DELETE_SUBNET_GROUP, {'deviceId': deviceId, 'subnetId': subnetId, 'groupId':groupId})

    def set_subnet_node(self, subnetId, name, ipAddress):
        """
        Assign a device node to a subnet

        Args:
            subnetId (Integer): Id of the subnet
            name (String): Name of the device node
            ipAddress (String): IPv4-Address of the device

        Returns:
            Json: Result
        """
        return self.__post(ASSING_SUBNET_NODE, {'subnetId': subnetId, 'name': name, 'ipAddress':ipAddress})

    def delete_subnet_node(self, node_id):
        """
        Delete a node device from a subnet

        Args:
            node_id (Integer): Id of the node

        Returns:
            Json: Result
        """
        return self.__delete(DELETE_SUBNET_NODE.format(node_id))

    def set_subnet_node_group(self, nodeId, groupId):
        """
        Assign a device node to a group

        Args:
            nodeId (Integer): Id of the device node
            groupId (Integer): Id of the group

        Returns:
            Json: Result
        """
        return self.__post(ASSIGN_SUBNET_NODE_GROUP, {'nodeId': nodeId, 'groupId': groupId})

    def delete_subnet_node_group(self, nodeId, groupId):
        """
        Remove a device node from a group

        Args:
            nodeId (Integer): Id of the device node
            groupId (Integer): Id of the group

        Returns:
            Json: Result
        """
        return self.__post(DELETE_SUBNET_NODE_GROUP, {'nodeId': nodeId, 'groupId': groupId})

    def create_group(self, name, description=None, communicationAllowed=None, lan1=None, lan2=None,lan3=None,lan4=None):
        """
        Create a new group

        Args:
            name (String): Name of the new group
            description (String, optional): Description of the new group. Defaults to None.
            communicationAllowed (Bool, optional): Can users and device communicate with each other. Defaults to None.
            lan1 (Bool, optional): Can LAN 1 be accessed. Defaults to None.
            lan2 (Bool, optional): Can LAN 2 be accessed. Defaults to None.
            lan3 (Bool, optional): Can LAN 3 be accessed. Defaults to None.
            lan4 (Bool, optional): Can LAN 4 be accessed. Defaults to None.

        Returns:
            Json: Result
        """
        json_param ={'name':name}

        if description:
            json_param['description'] = description
        
        if communicationAllowed:
            json_param['communicationAllowed'] = communicationAllowed

        if lan1:
            json_param['lan1'] = lan1

        if lan2:
            json_param['lan2'] = lan2

        if lan3:
            json_param['lan3'] = lan3

        if lan4:
            json_param['lan4'] = lan4

        return self.__post(CREATE_GROUP, json_param)

    def delete_group(self, group_id):
        """
        Delete a group

        Args:
            group_id (Integer): Group id, which should be deleted

        Returns:
            Json: Result
        """
        return self.__delete(DELETE_GROUP.format(group_id))

    def get_groups(self, search=None):
        """
        Get group information from server

        Args:
            search (String, optional): Filter string to look for specific group. Defaults to None.

        Returns:
            Json: Result
        """
        if search:
            return self.__get('{}?search={}'.format(GET_GROUPS, search))
        else:
            return self.__get(GET_GROUPS)

    def get_communication_relation(self, group_id):
        """
        Get the communication relations of a group

        Args:
            group_id (Integer): Id of a group

        Returns:
            Json: Result
        """
        return self.__get(GET_GROUP_RELATION.format(group_id))

    def set_communication_relation(self, group_partner_source, group_partner_destination):
        """
        Define a communication relation between two groups

        Args:
            group_partner_source (Integer): Id of starting group
            group_partner_destination (Integer): Id of destination group

        Returns:
            Json: Result
        """
        return self.__post(ASSIGN_GROUPS_RELATION.format(group_partner_source), {'destinationId': group_partner_destination})

    def delete_communication_relation(self, group_partner_source, group_partner_destination):
        """
        Remove a communication relation of two groups

        Args:
            group_partner_source (Integer): Id of starting group
            group_partner_destination (Integer): Id of destination group

        Returns:
            Json: Result
        """
        return self.__delete(DELETE_GROUPS_RELATION.format(group_partner_source), {'destinationId': group_partner_destination})

    def get_roles(self, search=None, role_id=None):
        """
        Get Role Details

        Args:
            search (String, optional): Filter string. Defaults to None.
            role_id (Integer, optional): Role id to get details for this specific role. Defaults to None.


        Returns:
            Json: Result
        """

        if role_id and search:
            raise src_wrong_usage(
                'Role_id and search can not be used at the same time')

        if role_id:
            return self.__get_role_details(role_id)
        else:
            if search:
                role_ids = self.__get('{}?search={}'.format(GET_ROLES, search))
            else:
                role_ids = self.__get(GET_ROLES)
            if role_ids['status_code'] == STATUS_OK:
                role_details = []
                for role in role_ids['data']:
                    role_details.append(self.__get_role_details(role['id']))
                return {'role_ids': role_ids['data'], 'role_details': role_details, 'status_code':role_ids['status_code']}
            else:
                return role_ids

    def __get_role_details(self, role_id):
        """
        Get details for a role

        Args:
            role_id (Integer): Role ids

        Returns:
            Json: Result
        """
        temp_role = self.__get(GET_ROLE_DETAIL.format(role_id))['data']
        temp_role['role_id'] = role_id
        return temp_role

    def delete_role(self, role_id):
        """
        Delete a specif role 

        Args:
            role_id (Integer): Role ids

        Returns:
            Json: Result
        """
        return self.__delete(DELETE_ROLE.format(role_id))

    def create_role(self, name, rights=None, passwordExpire=None, passwordReusing=None, passwordChangeFirstLogin=None, pkiDnFilterRule=None, pkiDeleteTmpUser=None, umcUserGroup=None, umcDeleteTmpUser=None):
        """
        Create a new user role

        Args:
            name (String): Name of this new role
            rights (List of integer, optional): List of right, which this role should have 1 = manage users and roles / 2 = create backup copies / 3 = restore the system / 4 = edit system parameters / 5 = manage devices / 6 = manage address spaces / 7 = manage remote connections / 8 = certificate management / 9 = manage firmware updates / 10 = force comment / 11 = download client software. Defaults to None.
            passwordExpire (Integer, optional): Parameter to set the password expiration. Defaults to None.
            passwordReusing (Integer, optional): Parameter to define how often the password can be reused. Defaults to None.
            passwordChangeFirstLogin (Bool, optional): Does the customer has to change the password. Defaults to None.
            pkiDnFilterRule (String, optional): Filter rule for PKI certificates. Defaults to None.
            pkiDeleteTmpUser (Integer, optional): Hours in which the temporary user will be deleted 1-72h, 0 is off. Defaults to None.
            umcUserGroup (String, optional): UMC group name which will be assigned to this group. Defaults to None.
            umcDeleteTmpUser (Integer, optional): Hours in which the temporary user will be deleted 1-72h, 0 is off. Defaults to None.

        Returns:
            Json: Result
        """
        temp_role = {'name': name}
        if rights:
            if isinstance(rights, str):
                rights = rights.split(',')
                rights = [int(numeric_string) for numeric_string in rights]
            temp_role['rights'] = rights

        if passwordExpire:
            temp_role['passwordExpire'] = passwordExpire

        if passwordReusing:
            temp_role['passwordReusing'] = passwordReusing

        if passwordChangeFirstLogin:
            temp_role['passwordChangeFirstLogin'] = passwordChangeFirstLogin

        if pkiDnFilterRule:
            temp_role['pkiDnFilterRule'] = pkiDnFilterRule

        if pkiDeleteTmpUser:
            temp_role['pkiDeleteTmpUser'] = pkiDeleteTmpUser

        if umcUserGroup:
            temp_role['umcUserGroup'] = umcUserGroup

        if umcDeleteTmpUser:
            temp_role['umcDeleteTmpUser'] = umcDeleteTmpUser
        return self.__post(CREATE_ROLES, temp_role)

    def get_users(self, search=None, user_id=None):
        """
        Get details about configured users

        Args:
            search (String, optional): Filter string for this search. Defaults to None.
            user_id (Integer, optional): Id of a user. Defaults to None.

        Raises:
            src_wrong_usage: user_id and search can't be used at the same time

        Returns:
            Json: Result
        """

        if user_id and search:
            raise src_wrong_usage(
                'user_id and search can not be used at the same time')

        if user_id:
            return self.__get_user_details(user_id)
        else:
            if search:
                user_ids = self.__get('{}?search={}'.format(GET_USERS, search))
            else:
                user_ids = self.__get(GET_USERS)
            if user_ids['status_code'] == STATUS_OK:
                user_details = []
                for user in user_ids['data']:
                    user_details.append(self.__get_user_details(user['id']))
                return {'user_ids': user_ids['data'], 'user_details': user_details, 'status_code':user_ids['status_code']}
            else:
                return user_ids

    def __get_user_details(self, user_id):
        """
        Get details about a specific user

        Args:
            user_id (Integer): Id of a specific user

        Returns:
            Json: Result
        """
        temp_user = self.__get(GET_USER_DETAIL.format(user_id))['data']
        temp_user['user_id'] = user_id
        temp_user['is_enabled'] = self.get_user_activation_status(user_id)[
            'data']['status']
        temp_groups = self.get_user_groups(user_id)
        if temp_groups['data']:
            temp_user['groups'] = temp_groups['data']
        temp_roles = self.get_user_roles(user_id)
        if temp_roles['data']:
            temp_user['roles'] = temp_roles['data']
        return temp_user

    def get_user_activation_status(self, user_id):
        """
        Check if a user is active and can be used

        Args:
            user_id (Integer): Id of a user

        Returns:
            Json: Result
        """
        return self.__get(GET_USER_ACTIVATION_STATUS.format(user_id))

    def get_user_groups(self, user_id):
        """
        Get all groups which are assigned to this user

        Args:
            user_id (Integer): Id of a user

        Returns:
            Json: Result
        """
        return self.__get(GET_USER_GROUPS.format(user_id))

    def get_user_roles(self, user_id):
        """
        Get all roles which are assigned to this user

        Args:
            user_id (Integer): Id of a user

        Returns:
            Json: Result
        """
        return self.__get(GET_USER_ROLES.format(user_id))

    def create_user(self, username, password, firstName=None, lastName=None, phone=None, email=None, loginMethod=1, pkiFilterRule=None, rights=None, fixedVpnAddress=None, groupId=None, roleId=None):
        """
        Create a new user

        Args:
            username (String): User name
            password (String): User password
            firstName (String, optional): First name. Defaults to None.
            lastName (String, optional): Second name. Defaults to None.
            phone (String, optional): Phone number. Defaults to None.
            email (String, optional): E-Mail address. Defaults to None.
            loginMethod (int, optional): Login method 1 for password and 2 for PKI. Defaults to 1.
            pkiFilterRule (String, optional): Filter rule. Defaults to None.
            rights (List of int, optional): List of int for user rights 1 = manage users and roles / 2 = create backup copies / 3 = restore the system / 4 = edit system parameters / 5 = manage devices / 6 = manage address spaces / 7 = manage remote connections / 8 = certificate management / 9 = manage firmware updates / 10 = force comment / 11 = download client software. Defaults to None.
            fixedVpnAddress (String, optional): IPv4-Address for this user in OpenVPN. Defaults to None.
            groupId (List of int or int, optional): Group ids which this user should be participating. Defaults to None.
            roleId (List of int or int, optional): Role ids which should be assigned to this user. Defaults to None.


        Returns:
            Json: Result
        """
        temp_user = {'username': username, 'password': password}

        if firstName:
            temp_user['firstName'] = firstName

        if lastName:
            temp_user['lastName'] = lastName

        if phone:
            temp_user['phone'] = phone

        if email:
            temp_user['email'] = email

        temp_user['loginMethod'] = loginMethod

        if pkiFilterRule:
            if loginMethod == 1:
                raise src_missing_value('For pki the loginMethod has to be 2')
            temp_user['pkiFilterRule'] = pkiFilterRule

        if rights:
            if isinstance(rights, str):
                rights = rights.split(',')
                rights = [int(numeric_string) for numeric_string in rights]
            temp_user['rights'] = rights

        if fixedVpnAddress:
            temp_user['fixedVpnAddress'] = fixedVpnAddress

        user = self.__post(CREATE_USER, parameter_json=temp_user)
        if user['status_code'] != STATUS_OK:
            return user
        user_id = user['data']['id']
        if groupId:
            if isinstance(groupId, list):
                for id in groupId:
                    result = self.assign_user_to_group(user_id, id)
                    if not result.__contains__('Accepted'):
                        return result
            else:
                result = self.assign_user_to_group(user_id, groupId)
                if not result.__contains__('Accepted'):
                    return result

        if roleId:
            if isinstance(roleId, list):
                for id in roleId:
                    result = self.assign_user_to_role(user_id, id)
                    if not result.__contains__('Accepted'):
                        return result
            else:
                result = self.assign_user_to_role(user_id, roleId)
                if not result.__contains__('Accepted'):
                    return result

        return user

    def assign_user_to_role(self, userId, roleId):
        """
        Assign a user to a role

        Args:
            userId (Integer): Id of the user
            roleId (Integer): Id of the role

        Returns:
            Json: Result
        """
        return self.__post(ASSIGN_USER_ROLE, {'userId': userId, 'roleId': roleId})

    def delete_user_from_role(self, userId, roleId):
        """
        Remove a user from a role

        Args:
            userId (Integer): Id of the user
            roleId (Integer): Id of the role

        Returns:
            Json: Result
        """
        return self.__post(DELETE_USER_ROLE, {'userId': userId, 'roleId': roleId})

    def assign_user_to_group(self, userId, groupId):
        """
        Assign a user to a group

        Args:
            userId (Integer): Id of the user
            groupId (Integer): Id of the group

        Returns:
            Json: Result
        """
        return self.__post(ASSIGN_USER_GROUP, {'userId': userId, 'groupId': groupId})

    def delete_user_from_group(self, userId, groupId):
        """
        Remove a user from a group

        Args:
            userId (Integer): Id of the user
            groupId (Integer): Id of the group

        Returns:
            Json: Result
        """
        return self.__delete(DELETE_USER_GROUP, {'userId': userId, 'groupId': groupId})

    def set_user_enabled_status(self, user_id, status=True):
        """
        Enable or disable a user

        Args:
            user_id (Integer): Id of the user
            status (bool, optional): Should the user be enabled or disabled. Defaults to True.

        Returns:
            Json: Result
        """
        return self.__put(SET_USER_ACTIVATION_STATUS.format(user_id), parameter_json={'status': status})

    def delete_user(self, user_id):
        """
        Delete a user

        Args:
            user_id (Integer): Id of a user

        Returns:
            Json: Result
        """
        return self.__delete(DELETE_USER.format(user_id))

    def get_current_webserver(self):
        """
        Get current webserver information, will also update object information

        Returns:
            Json: Result
        """
        data = self.__get(GET_CURRENT_WEBSERVER)
        self.__update_system_info(data)
        return data

    def get_user_agreement(self):
        """
        Get user agreement

        Returns:
            Json: Result
        """
        return self.__get(GET_USER_AGREEMENT)

    def set_user_agreement(self, displayOption, message):
        """
        Define a user agreement

        Args:
            displayOption (Integer): When should the user agreement be shown 0 = Never / 1 = Firsttime / 2 = Always
            message (String): Message of the user agreement

        Returns:
            Json: Result
        """
        user_agreement = {'displayOption': displayOption, 'message': message}
        return self.__post(SET_USER_AGREEMENT, parameter_json=user_agreement)

    def get_client_licenses(self, client_id=None):
        """
        Get information about used client licenses

        Args:
            client_id (Integer, optional): Define a information about a specific client entry. Defaults to None.

        Returns:
            Json: Result
        """
        if client_id:
            return self.__get(GET_CLIENT_LICENSE_DETAILS.format(client_id))

        client_id = self.__get(GET_CLIENT_LICENSE)
        if client_id['status_code'] == STATUS_OK:
            client_details = []
            for id in client_id['data']:
                client_details.append(
                    self.get_client_licenses(id['id'])['data'])
            client_id['details'] = client_details

        return client_id

    def delete_client_license(self, client_id):
        """
        Free a client license by deleting a client id

        Args:
            client_id (Integer): Id of client entry

        Returns:
            Json: Result
        """
        return self.__delete(DELETE_CLIENT_LICENSE.format(client_id))


    def get_user_log(self):
        """
        Retrieve complete user log from server
        """
        return self.__get(GET_USER_LOG.format())

    def get_user_to_influx(self, influx_client):
        """
        Retrieve log and push it to influx database

        Args:
            influx_client (InfluxDBClient): Python client for database
        """

    def set_webser_cert(self, path_to_cert, path_to_key, path_to_ca, password = None):
        """Upload new certificates to server

        Args:
            path_to_cert (Path): Path to cert file
            path_to_key (Path): Path to private key file
            path_to_ca (Path): Path to CA file
            password (String, optional): Optional password for files. Defaults to None.
        """
        files = {'certificate': open(path_to_cert,'rb'),
                'key': open(path_to_key,'rb'),
                'ca': open(path_to_ca,'rb')}
        if password:
            files['password'] = password
        return self.__post(SET_WEBSERVER_CERT, files=files)

    def __get_token(self):
        """
        Retrieve token from server

        Returns:
            Json: Result
        """
        json = {'username': self.username, 'password':self.password}
        path = TOKEN_PATH
        request_result = None
        try:

            headers = {"Accept": "application/json"}
            request_result = self.__session.post('{}{}'.format(self.base_uri, path),
                                                 json=json,
                                                 timeout=self.timeout,
                                                 verify=self.verify_certificate,
                                                 headers=headers)
        except Exception as ex:
            logging.error('Exception:{}'.format(ex))

        if request_result:
            if request_result.status_code == STATUS_FORBIDDEN:
                raise src_missing_rights('Missing privileges for API')
            result_json = request_result.json()
            self.__token = result_json[TOKEN_JSON_KEY]
            if self.__token:
                return True

        return False

    def __post(self,  path, parameter_json=None, files= None):
        result_json = {}
        if not self.__token:
            if not self.__get_token():
                raise src_missing_token('Missing token')
        try:

            headers = {"Accept": "application/json",
                       'Authorization': f'token {self.__token}'}
            if not files:
                request_result = self.__session.post('{}{}'.format(self.base_uri, path),
                                                    json=parameter_json,
                                                    timeout=self.timeout,
                                                    verify=self.verify_certificate,
                                                    headers=headers)
            else:
                request_result = self.__session.post('{}{}'.format(self.base_uri, path),
                                                    files=files,
                                                    timeout=self.timeout,
                                                    verify=self.verify_certificate,
                                                    headers=headers)
            result_json['status_code'] = request_result.status_code
            if request_result.content:
                result_json['data'] = request_result.json()
            else:
                result_json = self.__validate_status(
                    request_result.status_code)
        except Exception as ex:
            logging.error('Exception:{}'.format(ex))

        return result_json

    def __get(self,  path):
        result_json = {}
        if not self.__token:
            if not self.__get_token():
                raise src_missing_token('Missing token')
        try:

            headers = {"Accept": "application/json",
                       'Authorization': f'token {self.__token}'}
            request_result = self.__session.get('{}{}'.format(self.base_uri, path),
                                                timeout=self.timeout,
                                                verify=self.verify_certificate,
                                                headers=headers)

            result_json['status_code'] = request_result.status_code
            if request_result.content:
                result_json['data'] = request_result.json()
            else:
                result_json = self.__validate_status(
                    request_result.status_code)
        except Exception as ex:
            logging.error('Exception:{}'.format(ex))

        return result_json

    def __put(self,  path, parameter_json=None):
        result_json = {}
        if not self.__token:
            if not self.__get_token():
                raise src_missing_token('Missing token')
        try:

            headers = {"Accept": "application/json",
                       'Authorization': f'token {self.__token}'}
            request_result = self.__session.put('{}{}'.format(self.base_uri, path),
                                                json=parameter_json,
                                                timeout=self.timeout,
                                                verify=self.verify_certificate,
                                                headers=headers)

            result_json['status_code'] = request_result.status_code
            if request_result.content:
                result_json['data'] = request_result.json()
            else:
                result_json = self.__validate_status(
                    request_result.status_code)
        except Exception as ex:
            logging.error('Exception:{}'.format(ex))

        return result_json

    def __delete(self,  path, parameter_json=None):
        result_json = {}
        if not self.__token:
            if not self.__get_token():
                raise src_missing_token('Missing token')
        try:

            headers = {"Accept": "application/json",
                       'Authorization': f'token {self.__token}'}
            request_result = self.__session.delete('{}{}'.format(self.base_uri, path),
                                                   json=parameter_json,
                                                   timeout=self.timeout,
                                                   verify=self.verify_certificate,
                                                   headers=headers)
            result_json['status_code'] = request_result.status_code
            if request_result.content:
                result_json['data'] = request_result.json()
            else:
                result_json = self.__validate_status(
                    request_result.status_code)
        except Exception as ex:
            logging.error('Exception:{}'.format(ex))

        return result_json

    def __validate_status(self, request_status):
        result_json = {'status_code': request_status}
        if request_status == STATUS_ACCEPTED:
            result_json = {'Accepted': True}
        elif request_status == STATUS_FORBIDDEN:
            result_json = {'Forbidden': True}
        elif request_status == STATUS_NOT_FOUND:
            result_json = {'Not found': True}
        elif request_status == STATUS_UNAUTHORIZED:
            result_json = {'Unauthorized': True}
        elif request_status == STATUS_CONFLICT:
            result_json = {'Conflict': True}
        elif request_status == STATUS_UNPROCESSABLE_ENTRY:
            result_json = {'Unprocessable': True}
        elif request_status == STATUS_METHOD_NOT_ALLOWED:
            result_json = {'Method not allowed': True}
        elif request_status == STATUS_OK:
            result_json = {'Accepted': True}
        return result_json
