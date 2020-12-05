#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-authorizers.html
if __name__ == '__main__':
    """
	create-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-authorizer.html
	delete-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-authorizer.html
	describe-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-authorizer.html
	update-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-authorizer.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("iot", "list-authorizers", add_option_dict)