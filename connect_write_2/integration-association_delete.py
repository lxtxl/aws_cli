#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/delete-integration-association.html
if __name__ == '__main__':
    """
	create-integration-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-integration-association.html
	list-integration-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-integration-associations.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # integration-association-id : The identifier for the AppIntegration association.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "delete-integration-association", "instance-id", "integration-association-id", add_option_dict)
