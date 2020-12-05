#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-tags.html
if __name__ == '__main__':
    """
	create-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-tags.html
    """

    parameter_display_string = """
    # resource-arn : Placeholder documentation for __string
    # tag-keys : Placeholder documentation for __string
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("medialive", "delete-tags", "resource-arn", "tag-keys", add_option_dict)
