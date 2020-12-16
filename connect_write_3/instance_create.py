#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-instance.html
if __name__ == '__main__':
    """
	delete-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/delete-instance.html
	describe-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance.html
	list-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-instances.html
    """

    parameter_display_string = """
    # identity-management-type : The type of identity management for your Amazon Connect users.
Possible values:

SAML
CONNECT_MANAGED
EXISTING_DIRECTORY
    # inbound-calls-enabled | --no-inbound-calls-enabled : Whether your contact center handles incoming contacts.
    # outbound-calls-enabled | --no-outbound-calls-enabled : Whether your contact center allows outbound calls.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "create-instance", "identity-management-type", "inbound-calls-enabled | --no-inbound-calls-enabled", "outbound-calls-enabled | --no-outbound-calls-enabled", add_option_dict)
