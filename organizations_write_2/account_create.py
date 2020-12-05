#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-account.html
if __name__ == '__main__':
    """
	describe-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-account.html
	list-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-accounts.html
	move-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/move-account.html
    """

    parameter_display_string = """
    # email : The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account. You must use a valid email address to complete account creation. You canât access the root user of the account or remove an account that was created with an invalid email address.
    # account-name : The friendly name of the member account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "create-account", "email", "account-name", add_option_dict)
