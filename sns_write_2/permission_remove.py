#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/remove-permission.html
if __name__ == '__main__':
    """
	add-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/add-permission.html
    """

    parameter_display_string = """
    # topic-arn : The ARN of the topic whose access control policy you wish to modify.
    # label : The unique label of the statement you want to remove.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sns", "remove-permission", "topic-arn", "label", add_option_dict)
