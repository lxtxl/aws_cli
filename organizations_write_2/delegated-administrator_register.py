#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/register-delegated-administrator.html
if __name__ == '__main__':
    """
	deregister-delegated-administrator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/deregister-delegated-administrator.html
	list-delegated-administrators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-delegated-administrators.html
    """

    parameter_display_string = """
    # account-id : The account ID number of the member account in the organization to register as a delegated administrator.
    # service-principal : The service principal of the AWS service for which you want to make the member account a delegated administrator.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "register-delegated-administrator", "account-id", "service-principal", add_option_dict)
