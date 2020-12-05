#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/tag-resource.html
    """

    parameter_display_string = """
    # resource-id : Specifies the EFS resource that you want to remove tags from.
    # tag-keys : The keys of the key:value tag pairs that you want to remove from the specified EFS resource.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("efs", "untag-resource", "resource-id", "tag-keys", add_option_dict)
