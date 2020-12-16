#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-access-policies.html
if __name__ == '__main__':
    """
	create-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-access-policy.html
	delete-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-access-policy.html
	describe-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-access-policy.html
	update-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-access-policy.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("iotsitewise", "list-access-policies", add_option_dict)