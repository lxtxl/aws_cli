#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-retention-policy.html
if __name__ == '__main__':
    """
	put-retention-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-retention-policy.html
    """

    parameter_display_string = """
    # organization-id : The organization ID.
    # id : The retention policy ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workmail", "delete-retention-policy", "organization-id", "id", add_option_dict)
