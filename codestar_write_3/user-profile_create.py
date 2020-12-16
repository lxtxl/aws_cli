#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/create-user-profile.html
if __name__ == '__main__':
    """
	delete-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/delete-user-profile.html
	describe-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/describe-user-profile.html
	list-user-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-user-profiles.html
	update-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-user-profile.html
    """

    parameter_display_string = """
    # user-arn : The Amazon Resource Name (ARN) of the user in IAM.
    # display-name : The name that will be displayed as the friendly name for the user in AWS CodeStar.
    # email-address : The email address that will be displayed as part of the userâs profile in AWS CodeStar.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codestar", "create-user-profile", "user-arn", "display-name", "email-address", add_option_dict)
