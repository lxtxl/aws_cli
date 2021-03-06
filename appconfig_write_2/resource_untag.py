#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the resource for which to remove tags.
    # tag-keys : The tag keys to delete.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appconfig", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
