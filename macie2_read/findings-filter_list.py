#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-findings-filters.html
if __name__ == '__main__':
    """
	create-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-findings-filter.html
	delete-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-findings-filter.html
	get-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-findings-filter.html
	update-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-findings-filter.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("macie2", "list-findings-filters", add_option_dict)