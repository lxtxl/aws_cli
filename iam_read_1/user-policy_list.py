#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-policies.html
if __name__ == '__main__':
    """
	attach-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html
	delete-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-policy.html
	detach-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-user-policy.html
	get-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user-policy.html
	put-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-policy.html
    """

    parameter_display_string = """
    # user-name : The name of the user to list policies for.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("iam", "list-user-policies", "user-name", add_option_dict)