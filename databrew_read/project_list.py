#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-projects.html
if __name__ == '__main__':
    """
	create-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-project.html
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/delete-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-project.html
	update-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-project.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("databrew", "list-projects", add_option_dict)