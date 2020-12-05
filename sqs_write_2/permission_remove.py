#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/remove-permission.html
if __name__ == '__main__':
    """
	add-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/add-permission.html
    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue from which permissions are removed.
Queue URLs and names are case-sensitive.
    # label : The identification of the permission to remove. This is the label added using the ``  AddPermission `` action.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sqs", "remove-permission", "queue-url", "label", add_option_dict)
