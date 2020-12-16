#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/add-tags-to-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-type : Specifies the type of resource you are tagging.

Note
The ManagedInstance type for this API action is for on-premises managed instances. You must specify the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.

Possible values:

Document
ManagedInstance
MaintenanceWindow
Parameter
PatchBaseline
OpsItem
    # resource-id : The resource ID you want to tag.
Use the ID of the resource. Here are some examples:
ManagedInstance: mi-012345abcde
MaintenanceWindow: mw-012345abcde
PatchBaseline: pb-012345abcde
For the Document and Parameter values, use the name of the resource.

Note
The ManagedInstance type for this API action is only for on-premises managed instances. You must specify the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    # tags : One or more tags. The value parameter is required, but if you donât want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.

Warning
Do not enter personally identifiable information in this field.

(structure)

Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.
Key -> (string)

The name of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ssm", "add-tags-to-resource", "resource-type", "resource-id", "tags", add_option_dict)
