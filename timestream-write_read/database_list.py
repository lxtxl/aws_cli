#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/list-databases.html
if __name__ == '__main__':
    """
	create-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-database.html
	delete-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/delete-database.html
	describe-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/describe-database.html
	update-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/update-database.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("timestream-write", "list-databases", add_option_dict)