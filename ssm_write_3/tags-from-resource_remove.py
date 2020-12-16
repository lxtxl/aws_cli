#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/remove-tags-from-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-type : The type of resource from which you want to remove a tag.

Note
The ManagedInstance type for this API action is only for on-premises managed instances. Specify the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.

Possible values:

Document
ManagedInstance
MaintenanceWindow
Parameter
PatchBaseline
OpsItem
    # resource-id : The ID of the resource from which you want to remove tags. For example:
ManagedInstance: mi-012345abcde
MaintenanceWindow: mw-012345abcde
PatchBaseline: pb-012345abcde
For the Document and Parameter values, use the name of the resource.

Note
The ManagedInstance type for this API action is only for on-premises managed instances. Specify the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    # tag-keys : Tag keys that you want to remove from the specified resource.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ssm", "remove-tags-from-resource", "resource-type", "resource-id", "tag-keys", add_option_dict)
