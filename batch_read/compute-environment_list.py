#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-compute-environments.html
if __name__ == '__main__':
    """
	create-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-compute-environment.html
	delete-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-compute-environment.html
	update-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("batch", "describe-compute-environments", add_option_dict)