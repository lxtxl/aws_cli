#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user.html
if __name__ == '__main__':
    """
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-users.html
    """

    parameter_display_string = """
    # access-token : The access token from a request to delete a user.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cognito-idp", "delete-user", "access-token", add_option_dict)





