#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-solutions.html
if __name__ == '__main__':
    """
	create-solution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-solution.html
	delete-solution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-solution.html
	describe-solution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-solution.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("personalize", "list-solutions", add_option_dict)