#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-primary-email-address.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The organization that contains the user, group, or resource to update.
    # entity-id : The user, group, or resource to update.
    # email : The value of the email to be updated as primary.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workmail", "update-primary-email-address", "organization-id", "entity-id", "email", add_option_dict)
