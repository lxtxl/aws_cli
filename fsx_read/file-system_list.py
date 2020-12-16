#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-file-systems.html
if __name__ == '__main__':
    """
	create-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-file-system.html
	delete-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/delete-file-system.html
	update-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/update-file-system.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("fsx", "describe-file-systems", add_option_dict)