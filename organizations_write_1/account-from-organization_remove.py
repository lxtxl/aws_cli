#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/remove-account-from-organization.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The unique identifier (ID) of the member account that you want to remove from the organization.
The regex pattern for an account ID string requires exactly 12 digits.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("organizations", "remove-account-from-organization", "account-id", add_option_dict)





