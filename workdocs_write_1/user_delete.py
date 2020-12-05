#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-user.html
if __name__ == '__main__':
    """
	activate-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/activate-user.html
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-user.html
	deactivate-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/deactivate-user.html
	describe-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-users.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-user.html
    """

    parameter_display_string = """
    # user-id : The ID of the user.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workdocs", "delete-user", "user-id", add_option_dict)





