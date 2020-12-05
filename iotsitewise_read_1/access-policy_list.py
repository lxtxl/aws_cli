#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-access-policy.html
if __name__ == '__main__':
    """
	create-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-access-policy.html
	delete-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-access-policy.html
	list-access-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-access-policies.html
	update-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-access-policy.html
    """

    parameter_display_string = """
    # access-policy-id : The ID of the access policy.
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

    execute_one_parameter("iotsitewise", "describe-access-policy", "access-policy-id", add_option_dict)