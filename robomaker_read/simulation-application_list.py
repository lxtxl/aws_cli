#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-applications.html
if __name__ == '__main__':
    """
	create-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-simulation-application.html
	delete-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-simulation-application.html
	describe-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-application.html
	update-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-simulation-application.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("robomaker", "list-simulation-applications", add_option_dict)