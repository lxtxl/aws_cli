#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabulary-filters.html
if __name__ == '__main__':
    """
	create-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-vocabulary-filter.html
	delete-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary-filter.html
	get-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-vocabulary-filter.html
	update-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-vocabulary-filter.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("transcribe", "list-vocabulary-filters", add_option_dict)