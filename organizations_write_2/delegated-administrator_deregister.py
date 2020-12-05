#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/deregister-delegated-administrator.html
if __name__ == '__main__':
    """
	list-delegated-administrators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-delegated-administrators.html
	register-delegated-administrator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/register-delegated-administrator.html
    """

    parameter_display_string = """
    # account-id : The account ID number of the member account in the organization that you want to deregister as a delegated administrator.
    # service-principal : The service principal name of an AWS service for which the account is a delegated administrator.
Delegated administrator privileges are revoked for only the specified AWS service from the member account. If the specified service is the only service for which the member account is a delegated administrator, the operation also revokes Organizations read action permissions.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "deregister-delegated-administrator", "account-id", "service-principal", add_option_dict)
