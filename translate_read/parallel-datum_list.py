#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-parallel-data.html
if __name__ == '__main__':
    """
	create-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/create-parallel-data.html
	delete-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/delete-parallel-data.html
	get-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-parallel-data.html
	update-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/update-parallel-data.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("translate", "list-parallel-data", add_option_dict)