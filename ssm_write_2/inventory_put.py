#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-inventory.html
if __name__ == '__main__':
    """
	delete-inventory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-inventory.html
	get-inventory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-inventory.html
    """

    parameter_display_string = """
    # instance-id : An instance ID where you want to add or update inventory items.
    # items : The inventory items that you want to add or update on instances.
(structure)

Information collected from managed instances based on your inventory policy document
TypeName -> (string)

The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and AWS:WindowsUpdate.

SchemaVersion -> (string)

The schema version for the inventory item.

CaptureTime -> (string)

The time the inventory information was collected.

ContentHash -> (string)

MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API does not update the inventory item type contents if the MD5 hash has not changed since last update.

Content -> (list)

The inventory data of the inventory type.
(map)

key -> (string)
value -> (string)


Context -> (map)

A map of associated properties for a specified inventory type. For example, with this attribute, you can specify the ExecutionId , ExecutionType , ComplianceType properties of the AWS:ComplianceItem type.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "put-inventory", "instance-id", "items", add_option_dict)
