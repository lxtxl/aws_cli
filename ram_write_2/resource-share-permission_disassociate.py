#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share-permission.html
if __name__ == '__main__':
    """
	associate-resource-share-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/associate-resource-share-permission.html
	list-resource-share-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-resource-share-permissions.html
    """

    parameter_display_string = """
    # resource-share-arn : The Amazon Resource Name (ARN) of the resource share.
    # permission-arn : The ARN of the permission to disassociate from the resource share.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ram", "disassociate-resource-share-permission", "resource-share-arn", "permission-arn", add_option_dict)
