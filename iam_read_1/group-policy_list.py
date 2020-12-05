#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-group-policies.html
if __name__ == '__main__':
    """
	attach-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-group-policy.html
	delete-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group-policy.html
	detach-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-group-policy.html
	get-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group-policy.html
	put-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-group-policy.html
    """

    parameter_display_string = """
    # group-name : The name of the group to list policies for.
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

    execute_one_parameter("iam", "list-group-policies", "group-name", add_option_dict)