#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html
if __name__ == '__main__':
    """
	create-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html
	delete-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-specific-credential.html
	reset-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/reset-service-specific-credential.html
	update-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("iam", "list-service-specific-credentials", add_option_dict)