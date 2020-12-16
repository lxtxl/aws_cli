#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/list-environments.html
if __name__ == '__main__':
    """
	create-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/create-environment.html
	delete-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/delete-environment.html
	get-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/get-environment.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/update-environment.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("mwaa", "list-environments", add_option_dict)