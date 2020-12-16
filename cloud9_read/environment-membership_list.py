#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-memberships.html
if __name__ == '__main__':
    """
	create-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-membership.html
	delete-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment-membership.html
	update-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment-membership.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("cloud9", "describe-environment-memberships", add_option_dict)