#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-databases.html
if __name__ == '__main__':
    """
	create-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-database.html
	delete-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-database.html
	get-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-database.html
	update-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-database.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("glue", "get-databases", add_option_dict)