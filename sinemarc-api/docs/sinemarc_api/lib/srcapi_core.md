# Srcapi Core

[Sinemarc-api Index](../../README.md#sinemarc-api-index) /
[Sinemarc Api](../index.md#sinemarc-api) /
[Lib](./index.md#lib) /
Srcapi Core

> Auto-generated documentation for [sinemarc_api.lib.srcapi_core](../../../sinemarc_api/lib/srcapi_core.py) module.

- [Srcapi Core](#srcapi-core)
  - [src_api](#src_api)
    - [src_api().__assign_device_subnet](#src_api()__assign_device_subnet)
    - [src_api().__assign_subnet_node](#src_api()__assign_subnet_node)
    - [src_api().__assign_subnet_node_group](#src_api()__assign_subnet_node_group)
    - [src_api().__get_device_details](#src_api()__get_device_details)
    - [src_api().__get_role_details](#src_api()__get_role_details)
    - [src_api().__get_token](#src_api()__get_token)
    - [src_api().__get_user_details](#src_api()__get_user_details)
    - [src_api().__update_system_info](#src_api()__update_system_info)
    - [src_api().activate_license](#src_api()activate_license)
    - [src_api().assign_user_to_group](#src_api()assign_user_to_group)
    - [src_api().assign_user_to_role](#src_api()assign_user_to_role)
    - [src_api().create_device](#src_api()create_device)
    - [src_api().create_device_subnet](#src_api()create_device_subnet)
    - [src_api().create_group](#src_api()create_group)
    - [src_api().create_role](#src_api()create_role)
    - [src_api().create_static_route](#src_api()create_static_route)
    - [src_api().create_user](#src_api()create_user)
    - [src_api().delete_client_license](#src_api()delete_client_license)
    - [src_api().delete_communication_relation](#src_api()delete_communication_relation)
    - [src_api().delete_device](#src_api()delete_device)
    - [src_api().delete_device_group](#src_api()delete_device_group)
    - [src_api().delete_device_openvpn](#src_api()delete_device_openvpn)
    - [src_api().delete_device_subnet](#src_api()delete_device_subnet)
    - [src_api().delete_group](#src_api()delete_group)
    - [src_api().delete_role](#src_api()delete_role)
    - [src_api().delete_static_route](#src_api()delete_static_route)
    - [src_api().delete_subnet_group](#src_api()delete_subnet_group)
    - [src_api().delete_subnet_node](#src_api()delete_subnet_node)
    - [src_api().delete_subnet_node_group](#src_api()delete_subnet_node_group)
    - [src_api().delete_user](#src_api()delete_user)
    - [src_api().delete_user_from_group](#src_api()delete_user_from_group)
    - [src_api().delete_user_from_role](#src_api()delete_user_from_role)
    - [src_api().get_DNS_server](#src_api()get_dns_server)
    - [src_api().get_cli_commands](#src_api()get_cli_commands)
    - [src_api().get_client_licenses](#src_api()get_client_licenses)
    - [src_api().get_communication_relation](#src_api()get_communication_relation)
    - [src_api().get_current_webserver](#src_api()get_current_webserver)
    - [src_api().get_devices](#src_api()get_devices)
    - [src_api().get_groups](#src_api()get_groups)
    - [src_api().get_license_information](#src_api()get_license_information)
    - [src_api().get_network_interface_status](#src_api()get_network_interface_status)
    - [src_api().get_ntp_configuration](#src_api()get_ntp_configuration)
    - [src_api().get_roles](#src_api()get_roles)
    - [src_api().get_server_api_settings](#src_api()get_server_api_settings)
    - [src_api().get_server_status](#src_api()get_server_status)
    - [src_api().get_static_routes](#src_api()get_static_routes)
    - [src_api().get_user_activation_status](#src_api()get_user_activation_status)
    - [src_api().get_user_agreement](#src_api()get_user_agreement)
    - [src_api().get_user_groups](#src_api()get_user_groups)
    - [src_api().get_user_log](#src_api()get_user_log)
    - [src_api().get_user_roles](#src_api()get_user_roles)
    - [src_api().get_user_to_influx](#src_api()get_user_to_influx)
    - [src_api().get_users](#src_api()get_users)
    - [src_api().get_webserver_configuration](#src_api()get_webserver_configuration)
    - [src_api().release_license](#src_api()release_license)
    - [src_api().send_ping](#src_api()send_ping)
    - [src_api().server_init](#src_api()server_init)
    - [src_api().set_DNS_server](#src_api()set_dns_server)
    - [src_api().set_communication_relation](#src_api()set_communication_relation)
    - [src_api().set_device_group](#src_api()set_device_group)
    - [src_api().set_device_openvpn](#src_api()set_device_openvpn)
    - [src_api().set_device_status](#src_api()set_device_status)
    - [src_api().set_network_interface](#src_api()set_network_interface)
    - [src_api().set_ntp_configuration](#src_api()set_ntp_configuration)
    - [src_api().set_server_api_settings](#src_api()set_server_api_settings)
    - [src_api().set_subnet_group](#src_api()set_subnet_group)
    - [src_api().set_subnet_node](#src_api()set_subnet_node)
    - [src_api().set_subnet_node_group](#src_api()set_subnet_node_group)
    - [src_api().set_user_agreement](#src_api()set_user_agreement)
    - [src_api().set_user_enabled_status](#src_api()set_user_enabled_status)
    - [src_api().set_webser_cert](#src_api()set_webser_cert)
    - [src_api().set_webserver_configuration](#src_api()set_webserver_configuration)

## src_api

[Show source in srcapi_core.py:27](../../../sinemarc_api/lib/srcapi_core.py#L27)

#### Signature

```python
class src_api:
    def __init__(
        self,
        address,
        port=443,
        username="admin",
        password="admin",
        timeout=500,
        verify_certificate=False,
    ): ...
```

### src_api().__assign_device_subnet

[Show source in srcapi_core.py:646](../../../sinemarc_api/lib/srcapi_core.py#L646)

Assign a subnet to a device

#### Arguments

- `subnet_parameter` *Json* - Json with subnet parameter
- `device_id` *Integer* - Device id

#### Raises

- `src_wrong_usage` - Raise error if server doesn't allow this subnet

#### Signature

```python
def __assign_device_subnet(self, subnet_parameter, device_id): ...
```

### src_api().__assign_subnet_node

[Show source in srcapi_core.py:676](../../../sinemarc_api/lib/srcapi_core.py#L676)

Assign node to a subnet

#### Arguments

- `subnet_id` *integer* - subnet id
- `node` *json* - Parameter for the node

#### Signature

```python
def __assign_subnet_node(self, subnet_id, node): ...
```

### src_api().__assign_subnet_node_group

[Show source in srcapi_core.py:710](../../../sinemarc_api/lib/srcapi_core.py#L710)

Assign group access to a node within a subnet

#### Arguments

- `node_id` *integer* - Id of the node
- `group_id` *integer* - Id of the group

#### Returns

- `Json` - Result of configuration

#### Signature

```python
def __assign_subnet_node_group(self, node_id, group_id): ...
```

### src_api().__get_device_details

[Show source in srcapi_core.py:436](../../../sinemarc_api/lib/srcapi_core.py#L436)

Retrieve details for a specific device

#### Arguments

- `id` *Integer* - device id

#### Returns

- `Json` - With current details about devices

#### Signature

```python
def __get_device_details(self, id): ...
```

### src_api().__get_role_details

[Show source in srcapi_core.py:1024](../../../sinemarc_api/lib/srcapi_core.py#L1024)

Get details for a role

#### Arguments

- `role_id` *Integer* - Role ids

#### Returns

- `Json` - Result

#### Signature

```python
def __get_role_details(self, role_id): ...
```

### src_api().__get_token

[Show source in srcapi_core.py:1446](../../../sinemarc_api/lib/srcapi_core.py#L1446)

Retrieve token from server

#### Returns

- `Json` - Result

#### Signature

```python
def __get_token(self): ...
```

### src_api().__get_user_details

[Show source in srcapi_core.py:1131](../../../sinemarc_api/lib/srcapi_core.py#L1131)

Get details about a specific user

#### Arguments

- `user_id` *Integer* - Id of a specific user

#### Returns

- `Json` - Result

#### Signature

```python
def __get_user_details(self, user_id): ...
```

### src_api().__update_system_info

[Show source in srcapi_core.py:60](../../../sinemarc_api/lib/srcapi_core.py#L60)

Set basic information of webserver, which is needed to connect a device

#### Arguments

- `webserver` *Json* - Return result of get_current_webserver()

#### Signature

```python
def __update_system_info(self, webserver): ...
```

### src_api().activate_license

[Show source in srcapi_core.py:114](../../../sinemarc_api/lib/srcapi_core.py#L114)

Activate a new license on your SINEMA RC server

#### Arguments

- `ticketNo` *String* - Ticket ID which is provided on the certificate of license
- `amount` *Integer, optional* - Number of nodes of a user license, which should be activated. Defaults to None.

#### Returns

- `Json` - Result of activation

#### Signature

```python
def activate_license(self, ticketNo, amount=None): ...
```

### src_api().assign_user_to_group

[Show source in srcapi_core.py:1295](../../../sinemarc_api/lib/srcapi_core.py#L1295)

Assign a user to a group

#### Arguments

- `userId` *Integer* - Id of the user
- `groupId` *Integer* - Id of the group

#### Returns

- `Json` - Result

#### Signature

```python
def assign_user_to_group(self, userId, groupId): ...
```

### src_api().assign_user_to_role

[Show source in srcapi_core.py:1269](../../../sinemarc_api/lib/srcapi_core.py#L1269)

Assign a user to a role

#### Arguments

- `userId` *Integer* - Id of the user
- `roleId` *Integer* - Id of the role

#### Returns

- `Json` - Result

#### Signature

```python
def assign_user_to_role(self, userId, roleId): ...
```

### src_api().create_device

[Show source in srcapi_core.py:519](../../../sinemarc_api/lib/srcapi_core.py#L519)

Create a new vpn device

#### Arguments

- `name` *String* - Name of the device
- `password` *String* - Password which the device should use to logon
type (String or Integer): Device type can be name of type or number from manual
connectionType (String or Integer): How the connection should be established
- `vendor` *String, optional* - Name of vendor. Defaults to None.
- `smsGatewayProvider` *String, optional* - SMS gateway for wake-up SMS. Defaults to None.
- `gsmNumber` *String, optional* - Phone number of the device. Defaults to None.
- `senderId` *String, optional* - Authentication of SMS for RTU303xC. Defaults to None.
- `location` *String, optional* - Location of the device. Defaults to None.
- `comment` *String, optional* - Comment for the device. Defaults to None.
- `fixedVpnAddress` *String, optional* - OpenVPN address for the device. Defaults to None.
- `defaultGateway` *Bool, optional* - Is the device configured as default gateway within the machine. Defaults to None.
openvpn_parameter (Json or List of Json, optional): OpenVPN Parameter which should be used by the device. Defaults to None.
groupId (Integer or List of Integer, optional): All participant group ids, which should have access to the device. Defaults to None.
subnet_parameter (Json or List of Integer, optional): Subnet configuration. Defaults to None.
- `get_running_cli` *bool, optional* - Should a list of CLI commands be created to connect the device. Defaults to False.

#### Returns

- `Json` - With result of the creation

#### Signature

```python
def create_device(
    self,
    name,
    password,
    type,
    connectionType,
    vendor=None,
    smsGatewayProvider=None,
    gsmNumber=None,
    senderId=None,
    location=None,
    comment=None,
    fixedVpnAddress=None,
    defaultGateway=None,
    openvpn_parameter=None,
    groupId=None,
    subnet_parameter=None,
    get_running_cli=False,
): ...
```

### src_api().create_device_subnet

[Show source in srcapi_core.py:777](../../../sinemarc_api/lib/srcapi_core.py#L777)

Assign a subnet to a device

#### Arguments

- `deviceId` *integer* - Id of the device
- `name` *string* - Name of the subnet
- `ipAddress` *string* - IPv4-Address of the subnet
- `subnetMask` *string* - IPv4-Subnetmask of the subnet
- `natMode` *integer* - NAT-Modus: 0 = none / 1 = 1:1 NAT
- `virtualIp` *string, optional* - Virtual IPv4 for NAT. Defaults to None.

#### Returns

- `Json` - Result of configuration

#### Signature

```python
def create_device_subnet(
    self, deviceId, name, ipAddress, subnetMask, natMode, virtualIp=None
): ...
```

### src_api().create_group

[Show source in srcapi_core.py:889](../../../sinemarc_api/lib/srcapi_core.py#L889)

Create a new group

#### Arguments

- `name` *String* - Name of the new group
- `description` *String, optional* - Description of the new group. Defaults to None.
- `communicationAllowed` *Bool, optional* - Can users and device communicate with each other. Defaults to None.
- `lan1` *Bool, optional* - Can LAN 1 be accessed. Defaults to None.
- `lan2` *Bool, optional* - Can LAN 2 be accessed. Defaults to None.
- `lan3` *Bool, optional* - Can LAN 3 be accessed. Defaults to None.
- `lan4` *Bool, optional* - Can LAN 4 be accessed. Defaults to None.

#### Returns

- `Json` - Result

#### Signature

```python
def create_group(
    self,
    name,
    description=None,
    communicationAllowed=None,
    lan1=None,
    lan2=None,
    lan3=None,
    lan4=None,
): ...
```

### src_api().create_role

[Show source in srcapi_core.py:1050](../../../sinemarc_api/lib/srcapi_core.py#L1050)

Create a new user role

#### Arguments

- `name` *String* - Name of this new role
rights (List of integer, optional): List of right, which this role should have 1 = manage users and roles / 2 = create backup copies / 3 = restore the system / 4 = edit system parameters / 5 = manage devices / 6 = manage address spaces / 7 = manage remote connections / 8 = certificate management / 9 = manage firmware updates / 10 = force comment / 11 = download client software. Defaults to None.
- `passwordExpire` *Integer, optional* - Parameter to set the password expiration. Defaults to None.
- `passwordReusing` *Integer, optional* - Parameter to define how often the password can be reused. Defaults to None.
- `passwordChangeFirstLogin` *Bool, optional* - Does the customer has to change the password. Defaults to None.
- `pkiDnFilterRule` *String, optional* - Filter rule for PKI certificates. Defaults to None.
- `pkiDeleteTmpUser` *Integer, optional* - Hours in which the temporary user will be deleted 1-72h, 0 is off. Defaults to None.
- `umcUserGroup` *String, optional* - UMC group name which will be assigned to this group. Defaults to None.
- `umcDeleteTmpUser` *Integer, optional* - Hours in which the temporary user will be deleted 1-72h, 0 is off. Defaults to None.

#### Returns

- `Json` - Result

#### Signature

```python
def create_role(
    self,
    name,
    rights=None,
    passwordExpire=None,
    passwordReusing=None,
    passwordChangeFirstLogin=None,
    pkiDnFilterRule=None,
    pkiDeleteTmpUser=None,
    umcUserGroup=None,
    umcDeleteTmpUser=None,
): ...
```

### src_api().create_static_route

[Show source in srcapi_core.py:364](../../../sinemarc_api/lib/srcapi_core.py#L364)

Create a new static route

#### Arguments

- `destinationNetwork` *String* - IPv4-Address of destination network
- `networkMask` *String* - IPv4-Subnetmask for destination network
- `gateway` *String* - IPv4-Address of gateway
- `interface` *Integer* - The network interface which should be retrieved 0 = WAN / 1 = LAN1 / 2 = LAN2 / 3 = LAN3 / 4 = LAN4. Defaults to 0.

#### Returns

- `Json` - Result of configuration

#### Signature

```python
def create_static_route(self, destinationNetwork, networkMask, gateway, interface): ...
```

### src_api().create_user

[Show source in srcapi_core.py:1189](../../../sinemarc_api/lib/srcapi_core.py#L1189)

Create a new user

#### Arguments

- `username` *String* - User name
- `password` *String* - User password
- `firstName` *String, optional* - First name. Defaults to None.
- `lastName` *String, optional* - Second name. Defaults to None.
- `phone` *String, optional* - Phone number. Defaults to None.
- `email` *String, optional* - E-Mail address. Defaults to None.
- `loginMethod` *int, optional* - Login method 1 for password and 2 for PKI. Defaults to 1.
- `pkiFilterRule` *String, optional* - Filter rule. Defaults to None.
rights (List of int, optional): List of int for user rights 1 = manage users and roles / 2 = create backup copies / 3 = restore the system / 4 = edit system parameters / 5 = manage devices / 6 = manage address spaces / 7 = manage remote connections / 8 = certificate management / 9 = manage firmware updates / 10 = force comment / 11 = download client software. Defaults to None.
- `fixedVpnAddress` *String, optional* - IPv4-Address for this user in OpenVPN. Defaults to None.
groupId (List of int or int, optional): Group ids which this user should be participating. Defaults to None.
roleId (List of int or int, optional): Role ids which should be assigned to this user. Defaults to None.

#### Returns

- `Json` - Result

#### Signature

```python
def create_user(
    self,
    username,
    password,
    firstName=None,
    lastName=None,
    phone=None,
    email=None,
    loginMethod=1,
    pkiFilterRule=None,
    rights=None,
    fixedVpnAddress=None,
    groupId=None,
    roleId=None,
): ...
```

### src_api().delete_client_license

[Show source in srcapi_core.py:1403](../../../sinemarc_api/lib/srcapi_core.py#L1403)

Free a client license by deleting a client id

#### Arguments

- `client_id` *Integer* - Id of client entry

#### Returns

- `Json` - Result

#### Signature

```python
def delete_client_license(self, client_id): ...
```

### src_api().delete_communication_relation

[Show source in srcapi_core.py:979](../../../sinemarc_api/lib/srcapi_core.py#L979)

Remove a communication relation of two groups

#### Arguments

- `group_partner_source` *Integer* - Id of starting group
- `group_partner_destination` *Integer* - Id of destination group

#### Returns

- `Json` - Result

#### Signature

```python
def delete_communication_relation(
    self, group_partner_source, group_partner_destination
): ...
```

### src_api().delete_device

[Show source in srcapi_core.py:507](../../../sinemarc_api/lib/srcapi_core.py#L507)

Delete a device

#### Arguments

- `id` *Integer* - Device_id which should be deleted

#### Returns

- `Json` - Result of deletion

#### Signature

```python
def delete_device(self, id): ...
```

### src_api().delete_device_group

[Show source in srcapi_core.py:764](../../../sinemarc_api/lib/srcapi_core.py#L764)

Remove a device from a group

#### Arguments

- `deviceId` *Integer* - Id of the device
- `groupId` *Integer* - Id of the group

#### Returns

- `Json` - Result of delete

#### Signature

```python
def delete_device_group(self, deviceId, groupId): ...
```

### src_api().delete_device_openvpn

[Show source in srcapi_core.py:739](../../../sinemarc_api/lib/srcapi_core.py#L739)

Delete static OpenVPN configuration of a device

#### Arguments

- `id` *Integer* - Id of the openvpn paramater set

#### Returns

- `Json` - result of delete

#### Signature

```python
def delete_device_openvpn(self, id): ...
```

### src_api().delete_device_subnet

[Show source in srcapi_core.py:797](../../../sinemarc_api/lib/srcapi_core.py#L797)

Delete a subnet from a device

#### Arguments

- `subnet_id` *Integer* - Id of the subnet

#### Returns

- `Json` - Result of delete

#### Signature

```python
def delete_device_subnet(self, subnet_id): ...
```

### src_api().delete_group

[Show source in srcapi_core.py:927](../../../sinemarc_api/lib/srcapi_core.py#L927)

Delete a group

#### Arguments

- `group_id` *Integer* - Group id, which should be deleted

#### Returns

- `Json` - Result

#### Signature

```python
def delete_group(self, group_id): ...
```

### src_api().delete_role

[Show source in srcapi_core.py:1038](../../../sinemarc_api/lib/srcapi_core.py#L1038)

Delete a specif role

#### Arguments

- `role_id` *Integer* - Role ids

#### Returns

- `Json` - Result

#### Signature

```python
def delete_role(self, role_id): ...
```

### src_api().delete_static_route

[Show source in srcapi_core.py:381](../../../sinemarc_api/lib/srcapi_core.py#L381)

#### Signature

```python
def delete_static_route(self, id): ...
```

### src_api().delete_subnet_group

[Show source in srcapi_core.py:823](../../../sinemarc_api/lib/srcapi_core.py#L823)

Delete a subnet from a group

#### Arguments

- `deviceId` *Integer* - Id of the affected device
- `subnetId` *Integer* - Id of the affected subnet
- `groupId` *Integer* - Id of the whished group

#### Returns

- `Json` - Result

#### Signature

```python
def delete_subnet_group(self, deviceId, subnetId, groupId): ...
```

### src_api().delete_subnet_node

[Show source in srcapi_core.py:851](../../../sinemarc_api/lib/srcapi_core.py#L851)

Delete a node device from a subnet

#### Arguments

- `node_id` *Integer* - Id of the node

#### Returns

- `Json` - Result

#### Signature

```python
def delete_subnet_node(self, node_id): ...
```

### src_api().delete_subnet_node_group

[Show source in srcapi_core.py:876](../../../sinemarc_api/lib/srcapi_core.py#L876)

Remove a device node from a group

#### Arguments

- `nodeId` *Integer* - Id of the device node
- `groupId` *Integer* - Id of the group

#### Returns

- `Json` - Result

#### Signature

```python
def delete_subnet_node_group(self, nodeId, groupId): ...
```

### src_api().delete_user

[Show source in srcapi_core.py:1334](../../../sinemarc_api/lib/srcapi_core.py#L1334)

Delete a user

#### Arguments

- `user_id` *Integer* - Id of a user

#### Returns

- `Json` - Result

#### Signature

```python
def delete_user(self, user_id): ...
```

### src_api().delete_user_from_group

[Show source in srcapi_core.py:1308](../../../sinemarc_api/lib/srcapi_core.py#L1308)

Remove a user from a group

#### Arguments

- `userId` *Integer* - Id of the user
- `groupId` *Integer* - Id of the group

#### Returns

- `Json` - Result

#### Signature

```python
def delete_user_from_group(self, userId, groupId): ...
```

### src_api().delete_user_from_role

[Show source in srcapi_core.py:1282](../../../sinemarc_api/lib/srcapi_core.py#L1282)

Remove a user from a role

#### Arguments

- `userId` *Integer* - Id of the user
- `roleId` *Integer* - Id of the role

#### Returns

- `Json` - Result

#### Signature

```python
def delete_user_from_role(self, userId, roleId): ...
```

### src_api().get_DNS_server

[Show source in srcapi_core.py:106](../../../sinemarc_api/lib/srcapi_core.py#L106)

Get current DNS Configuration

#### Returns

- `Json` - current DNS Configuration

#### Signature

```python
def get_DNS_server(self): ...
```

### src_api().get_cli_commands

[Show source in srcapi_core.py:632](../../../sinemarc_api/lib/srcapi_core.py#L632)

Get CLI command for a device to connect it with SINEMA RC

#### Arguments

- `device_id` *Integer* - Id of the device which was returned by create device
- `device_password` *String* - Password for the device to logon

#### Returns

- `String` - CLI Commands for the device

#### Signature

```python
def get_cli_commands(self, device_id, device_password): ...
```

### src_api().get_client_licenses

[Show source in srcapi_core.py:1380](../../../sinemarc_api/lib/srcapi_core.py#L1380)

Get information about used client licenses

#### Arguments

- `client_id` *Integer, optional* - Define a information about a specific client entry. Defaults to None.

#### Returns

- `Json` - Result

#### Signature

```python
def get_client_licenses(self, client_id=None): ...
```

### src_api().get_communication_relation

[Show source in srcapi_core.py:954](../../../sinemarc_api/lib/srcapi_core.py#L954)

Get the communication relations of a group

#### Arguments

- `group_id` *Integer* - Id of a group

#### Returns

- `Json` - Result

#### Signature

```python
def get_communication_relation(self, group_id): ...
```

### src_api().get_current_webserver

[Show source in srcapi_core.py:1346](../../../sinemarc_api/lib/srcapi_core.py#L1346)

Get current webserver information, will also update object information

#### Returns

- `Json` - Result

#### Signature

```python
def get_current_webserver(self): ...
```

### src_api().get_devices

[Show source in srcapi_core.py:402](../../../sinemarc_api/lib/srcapi_core.py#L402)

Get current devices, which are configured

#### Arguments

- `device_id` *Integer, optional* - Device id to get details for this device. Defaults to None.
- `search` *String, optional* - Search string to filter for specific devices. Defaults to None.

#### Raises

- `src_wrong_usage` - device_id and search string can't be used at the same time

#### Returns

- `Json` - With Details about all devices, which were requested

#### Signature

```python
def get_devices(self, device_id=None, search=None): ...
```

### src_api().get_groups

[Show source in srcapi_core.py:939](../../../sinemarc_api/lib/srcapi_core.py#L939)

Get group information from server

#### Arguments

- `search` *String, optional* - Filter string to look for specific group. Defaults to None.

#### Returns

- `Json` - Result

#### Signature

```python
def get_groups(self, search=None): ...
```

### src_api().get_license_information

[Show source in srcapi_core.py:134](../../../sinemarc_api/lib/srcapi_core.py#L134)

Get information of current active licenses

#### Returns

- `Json` - License information

#### Signature

```python
def get_license_information(self): ...
```

### src_api().get_network_interface_status

[Show source in srcapi_core.py:211](../../../sinemarc_api/lib/srcapi_core.py#L211)

Get information about network configuration

#### Arguments

- `interface_id` *int, optional* - The network interface which should be retrieved 0 = WAN / 1 = LAN1 / 2 = LAN2 / 3 = LAN3 / 4 = LAN4. Defaults to 0.

#### Raises

- `src_wrong_datatype` - Error if interface_id is wrongly used

#### Returns

- `Json` - Current network status

#### Signature

```python
def get_network_interface_status(self, interface_id=0): ...
```

### src_api().get_ntp_configuration

[Show source in srcapi_core.py:384](../../../sinemarc_api/lib/srcapi_core.py#L384)

#### Signature

```python
def get_ntp_configuration(self): ...
```

### src_api().get_roles

[Show source in srcapi_core.py:992](../../../sinemarc_api/lib/srcapi_core.py#L992)

Get Role Details

#### Arguments

- `search` *String, optional* - Filter string. Defaults to None.
- `role_id` *Integer, optional* - Role id to get details for this specific role. Defaults to None.

#### Returns

- `Json` - Result

#### Signature

```python
def get_roles(self, search=None, role_id=None): ...
```

### src_api().get_server_api_settings

[Show source in srcapi_core.py:176](../../../sinemarc_api/lib/srcapi_core.py#L176)

Get current api settings

#### Returns

- `Json` - Current API settings

#### Signature

```python
def get_server_api_settings(self): ...
```

### src_api().get_server_status

[Show source in srcapi_core.py:203](../../../sinemarc_api/lib/srcapi_core.py#L203)

Get basic information about the server status

#### Returns

- `Json` - Information about the overview and current load of the server

#### Signature

```python
def get_server_status(self): ...
```

### src_api().get_static_routes

[Show source in srcapi_core.py:340](../../../sinemarc_api/lib/srcapi_core.py#L340)

Get static route of the server

#### Returns

- `Json` - Current configured static routes

#### Signature

```python
def get_static_routes(self): ...
```

### src_api().get_user_activation_status

[Show source in srcapi_core.py:1153](../../../sinemarc_api/lib/srcapi_core.py#L1153)

Check if a user is active and can be used

#### Arguments

- `user_id` *Integer* - Id of a user

#### Returns

- `Json` - Result

#### Signature

```python
def get_user_activation_status(self, user_id): ...
```

### src_api().get_user_agreement

[Show source in srcapi_core.py:1357](../../../sinemarc_api/lib/srcapi_core.py#L1357)

Get user agreement

#### Returns

- `Json` - Result

#### Signature

```python
def get_user_agreement(self): ...
```

### src_api().get_user_groups

[Show source in srcapi_core.py:1165](../../../sinemarc_api/lib/srcapi_core.py#L1165)

Get all groups which are assigned to this user

#### Arguments

- `user_id` *Integer* - Id of a user

#### Returns

- `Json` - Result

#### Signature

```python
def get_user_groups(self, user_id): ...
```

### src_api().get_user_log

[Show source in srcapi_core.py:1416](../../../sinemarc_api/lib/srcapi_core.py#L1416)

Retrieve complete user log from server

#### Signature

```python
def get_user_log(self): ...
```

### src_api().get_user_roles

[Show source in srcapi_core.py:1177](../../../sinemarc_api/lib/srcapi_core.py#L1177)

Get all roles which are assigned to this user

#### Arguments

- `user_id` *Integer* - Id of a user

#### Returns

- `Json` - Result

#### Signature

```python
def get_user_roles(self, user_id): ...
```

### src_api().get_user_to_influx

[Show source in srcapi_core.py:1422](../../../sinemarc_api/lib/srcapi_core.py#L1422)

Retrieve log and push it to influx database

#### Arguments

- `influx_client` *InfluxDBClient* - Python client for database

#### Signature

```python
def get_user_to_influx(self, influx_client): ...
```

### src_api().get_users

[Show source in srcapi_core.py:1097](../../../sinemarc_api/lib/srcapi_core.py#L1097)

Get details about configured users

#### Arguments

- `search` *String, optional* - Filter string for this search. Defaults to None.
- `user_id` *Integer, optional* - Id of a user. Defaults to None.

#### Raises

- `src_wrong_usage` - user_id and search can't be used at the same time

#### Returns

- `Json` - Result

#### Signature

```python
def get_users(self, search=None, user_id=None): ...
```

### src_api().get_webserver_configuration

[Show source in srcapi_core.py:296](../../../sinemarc_api/lib/srcapi_core.py#L296)

Get current webserver port configuration

#### Returns

- `Json` - Current webserver configuration

#### Signature

```python
def get_webserver_configuration(self): ...
```

### src_api().release_license

[Show source in srcapi_core.py:152](../../../sinemarc_api/lib/srcapi_core.py#L152)

Release license from server

#### Arguments

- `ticketNo` *String* - Ticket ID which is provided on the certificate of license

#### Returns

- `Json` - Result of release

#### Signature

```python
def release_license(self, ticketNo): ...
```

### src_api().send_ping

[Show source in srcapi_core.py:320](../../../sinemarc_api/lib/srcapi_core.py#L320)

Send ping from server to an address

#### Arguments

- `Address` *String* - IP-Address or DNS name of target dervice
- `repeat` *Integer, optional* - How often the ping should be send. Defaults to None.
- `timeout` *Integer, optional* - How long the server should wait for a reply. Defaults to None.

#### Returns

- `Json` - output if the ping was successful

#### Signature

```python
def send_ping(self, Address, repeat=None, timeout=None): ...
```

### src_api().server_init

[Show source in srcapi_core.py:163](../../../sinemarc_api/lib/srcapi_core.py#L163)

Set server after installation, this can only be used if no one was over locked on

#### Arguments

- `superAdmin` *String* - User is in default admin
- `superAdminPw` *String* - Password is in default admin

#### Returns

- `Json` - Result of init

#### Signature

```python
def server_init(self, superAdmin, superAdminPw): ...
```

### src_api().set_DNS_server

[Show source in srcapi_core.py:84](../../../sinemarc_api/lib/srcapi_core.py#L84)

Configure DNS Server on SINEMA RC Server

#### Arguments

- `hostname` *String* - DNS Name of the SINEMA RC Server
- `externallyResolvable` *Boolean, optional* - Is the hostname a resolvable DNS name. Defaults to None.
- `dnsPrimary` *String, optional* - IP-Address of main DNS Server. Defaults to None.
- `dnsSecondary` *String, optional* - IP-Address of Backup DNS Server. Defaults to None.

#### Returns

- `Json` - Result of request

#### Signature

```python
def set_DNS_server(
    self, hostname, externallyResolvable=None, dnsPrimary=None, dnsSecondary=None
): ...
```

### src_api().set_communication_relation

[Show source in srcapi_core.py:966](../../../sinemarc_api/lib/srcapi_core.py#L966)

Define a communication relation between two groups

#### Arguments

- `group_partner_source` *Integer* - Id of starting group
- `group_partner_destination` *Integer* - Id of destination group

#### Returns

- `Json` - Result

#### Signature

```python
def set_communication_relation(
    self, group_partner_source, group_partner_destination
): ...
```

### src_api().set_device_group

[Show source in srcapi_core.py:751](../../../sinemarc_api/lib/srcapi_core.py#L751)

Assign a device to a group

#### Arguments

- `deviceId` *Integer* - Id of the device
- `groupId` *Integer* - Id of the group

#### Returns

- `Json` - Result of configuration

#### Signature

```python
def set_device_group(self, deviceId, groupId): ...
```

### src_api().set_device_openvpn

[Show source in srcapi_core.py:723](../../../sinemarc_api/lib/srcapi_core.py#L723)

Configure the static OpenVPN settings which should be used by the device, without this the configuration will be created automatically

#### Arguments

- `deviceId` *Integer* - Id of the device
- `ipAddress` *String* - IP Address of OpenVPN server
- `port` *Integer* - Port of OpenVPN server
- `protocol` *String* - Protocol which should be used TCP or UDP

#### Returns

- `Json` - Result of configuration

#### Signature

```python
def set_device_openvpn(self, deviceId, ipAddress, port, protocol): ...
```

### src_api().set_device_status

[Show source in srcapi_core.py:493](../../../sinemarc_api/lib/srcapi_core.py#L493)

Enable or disable a device

#### Arguments

- `id` *Integer* - Device_id which should be enabled/disabled
- `status` *Bool* - Enabled/Disabled

#### Returns

- `Json` - Result of configuration

#### Signature

```python
def set_device_status(self, id, status): ...
```

### src_api().set_network_interface

[Show source in srcapi_core.py:228](../../../sinemarc_api/lib/srcapi_core.py#L228)

Configure a network interface

#### Arguments

- `interface_id` *integer, optional* - The network interface which should be retrieved 0 = WAN / 1 = LAN1 / 2 = LAN2 / 3 = LAN3 / 4 = LAN4. Defaults to 0.
- `dhcp` *Bool, optional* - Should DHCP be used to configure the network interface. Defaults to None.
ipAddress (String optional): Static IPv4-Address. Defaults to None.
- `networkMask` *String, optional* - Static IPv4-Subnet Mask. Defaults to None.
- `gateway` *String, optional* - Static IPv4-Address for default gateway. Defaults to None.
- `MTU` *Integer, optional* - MTU size. Defaults to None.
- `wanIp` *String, optional* - External IPv4-Address of NAT router. Defaults to None.
- `ipv6Enabled` *Bool, optional* - Should IPv6 enabled. Defaults to None.
- `ipv6Slaac` *Bool, optional* - Should IPv6 be configured via Claac. Defaults to None.
- `ipv6Address` *String, optional* - Static IPv6-Address. Defaults to None.
- `ipv6PrefixLength` *String, optional* - Static IPv6-Prefix Length. Defaults to None.
- `ipv6Gateway` *String, optional* - Static IPv6-Address for default gateway. Defaults to None.
- `masquerading` *Bool, optional* - Should every packet, which is send be the interface, be source natted. Defaults to None.

#### Raises

- `src_wrong_datatype` - Error if interface_id is wrongly used
- `src_missing_value` - If there are errors for Slaac vs Static IPv6 configuration

#### Returns

- `Json` - Result of network configuration

#### Signature

```python
def set_network_interface(
    self,
    interface_id,
    dhcp=None,
    ipAddress=None,
    networkMask=None,
    gateway=None,
    MTU=None,
    wanIp=None,
    ipv6Enabled=None,
    ipv6Slaac=None,
    ipv6Address=None,
    ipv6PrefixLength=None,
    ipv6Gateway=None,
    masquerading=None,
): ...
```

### src_api().set_ntp_configuration

[Show source in srcapi_core.py:387](../../../sinemarc_api/lib/srcapi_core.py#L387)

#### Signature

```python
def set_ntp_configuration(
    self, active, primaryNtp=None, secondNtp=None, timezone=None
): ...
```

### src_api().set_server_api_settings

[Show source in srcapi_core.py:184](../../../sinemarc_api/lib/srcapi_core.py#L184)

Configure api settings

#### Arguments

- `active` *bool, optional* - Activate or deactivate the server. Defaults to True.
- `startTrial` *bool, optional* - Start the 14 days trial phase. Defaults to None.
- `tokenExpireTime` *Integer, optional* - Number of days in which the authentication token is valid. Defaults to None.

#### Returns

- `Json` - Result of configuration

#### Signature

```python
def set_server_api_settings(
    self, active=True, startTrial=None, tokenExpireTime=None
): ...
```

### src_api().set_subnet_group

[Show source in srcapi_core.py:809](../../../sinemarc_api/lib/srcapi_core.py#L809)

Assign a subnet to a group

#### Arguments

- `deviceId` *Integer* - Id of the affected device
- `subnetId` *Integer* - Id of the affected subnet
- `groupId` *Integer* - Id of the whished group

#### Returns

- `Json` - Result

#### Signature

```python
def set_subnet_group(self, deviceId, subnetId, groupId): ...
```

### src_api().set_subnet_node

[Show source in srcapi_core.py:837](../../../sinemarc_api/lib/srcapi_core.py#L837)

Assign a device node to a subnet

#### Arguments

- `subnetId` *Integer* - Id of the subnet
- `name` *String* - Name of the device node
- `ipAddress` *String* - IPv4-Address of the device

#### Returns

- `Json` - Result

#### Signature

```python
def set_subnet_node(self, subnetId, name, ipAddress): ...
```

### src_api().set_subnet_node_group

[Show source in srcapi_core.py:863](../../../sinemarc_api/lib/srcapi_core.py#L863)

Assign a device node to a group

#### Arguments

- `nodeId` *Integer* - Id of the device node
- `groupId` *Integer* - Id of the group

#### Returns

- `Json` - Result

#### Signature

```python
def set_subnet_node_group(self, nodeId, groupId): ...
```

### src_api().set_user_agreement

[Show source in srcapi_core.py:1366](../../../sinemarc_api/lib/srcapi_core.py#L1366)

Define a user agreement

#### Arguments

- `displayOption` *Integer* - When should the user agreement be shown 0 = Never / 1 = Firsttime / 2 = Always
- `message` *String* - Message of the user agreement

#### Returns

- `Json` - Result

#### Signature

```python
def set_user_agreement(self, displayOption, message): ...
```

### src_api().set_user_enabled_status

[Show source in srcapi_core.py:1321](../../../sinemarc_api/lib/srcapi_core.py#L1321)

Enable or disable a user

#### Arguments

- `user_id` *Integer* - Id of the user
- `status` *bool, optional* - Should the user be enabled or disabled. Defaults to True.

#### Returns

- `Json` - Result

#### Signature

```python
def set_user_enabled_status(self, user_id, status=True): ...
```

### src_api().set_webser_cert

[Show source in srcapi_core.py:1430](../../../sinemarc_api/lib/srcapi_core.py#L1430)

Upload new certificates to server

#### Arguments

- `path_to_cert` *Path* - Path to cert file
- `path_to_key` *Path* - Path to private key file
- `path_to_ca` *Path* - Path to CA file
- `password` *String, optional* - Optional password for files. Defaults to None.

#### Signature

```python
def set_webser_cert(self, path_to_cert, path_to_key, path_to_ca, password=None): ...
```

### src_api().set_webserver_configuration

[Show source in srcapi_core.py:304](../../../sinemarc_api/lib/srcapi_core.py#L304)

Configure webserver ports

#### Arguments

- `httpsPort` *Integer* - Configure main port for website
- `fallBackPort` *Integer, optional* - Configure fallback port for device fallback of the webserver. Defaults to None.

#### Returns

- `Json` - Result of configuration

#### Signature

```python
def set_webserver_configuration(self, httpsPort, fallBackPort=None): ...
```