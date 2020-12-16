#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-approved-origin.html
if __name__ == '__main__':
    """
	disassociate-approved-origin : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-approved-origin.html
	list-approved-origins : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-approved-origins.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # origin : The domain to add to your allow list.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "associate-approved-origin", "instance-id", "origin", add_option_dict)
