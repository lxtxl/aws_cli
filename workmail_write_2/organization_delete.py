#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-organization.html
if __name__ == '__main__':
    """
	create-organization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-organization.html
	describe-organization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-organization.html
	list-organizations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-organizations.html
    """

    parameter_display_string = """
    # organization-id : The organization ID.
    # delete-directory | --no-delete-directory : If true, deletes the AWS Directory Service directory associated with the organization.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workmail", "delete-organization", "organization-id", "delete-directory | --no-delete-directory", add_option_dict)
