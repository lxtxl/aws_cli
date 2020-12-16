#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/put-resource-attributes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # progress-update-stream : The name of the ProgressUpdateStream.
    # migration-task-name : Unique identifier that references the migration task. Do not store personal data in this field.
    # resource-attribute-list : Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service repository.

Note
Takes the object array of ResourceAttribute where the Type field is reserved for the following values: IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER where the identifying value can be a string up to 256 characters.


Warning

If any âVMâ related value is set for a ResourceAttribute object, it is required that VM_MANAGER_ID , as a minimum, is always set. If VM_MANAGER_ID is not set, then all âVMâ fields will be discarded and âVMâ fields will not be used for matching the migration task to a server in Application Discovery Service repository. See the Example section below for a use case of specifying âVMâ related values.
If a server you are trying to match has multiple IP or MAC addresses, you should provide as many as you know in separate type/value pairs passed to the ResourceAttributeList parameter to maximize the chances of matching.


(structure)

Attribute associated with a resource.
Note the corresponding format required per type listed below:


IPV4

x.x.x.x
where x is an integer in the range [0,255]

IPV6

y : y : y : y : y : y : y : y
where y is a hexadecimal between 0 and FFFF. [0, FFFF]

MAC_ADDRESS

^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$

FQDN

^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$

Type -> (string)

Type of resource.

Value -> (string)

Value of the resource type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("mgh", "put-resource-attributes", "progress-update-stream", "migration-task-name", "resource-attribute-list", add_option_dict)
