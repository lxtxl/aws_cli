#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/remove-tags.html
if __name__ == '__main__':
    """
	add-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-tags.html
    """

    parameter_display_string = """
    # resource-arns : The Amazon Resource Name (ARN) of the resource.
(string)
    # tag-keys : The tag keys for the tags to remove.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "remove-tags", "resource-arns", "tag-keys", add_option_dict)
