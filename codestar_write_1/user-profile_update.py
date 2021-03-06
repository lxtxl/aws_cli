#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-user-profile.html
if __name__ == '__main__':
    """
	create-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/create-user-profile.html
	delete-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/delete-user-profile.html
	describe-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/describe-user-profile.html
	list-user-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-user-profiles.html
    """

    parameter_display_string = """
    # user-arn : The name that will be displayed as the friendly name for the user in AWS CodeStar.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codestar", "update-user-profile", "user-arn", add_option_dict)





