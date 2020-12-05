#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-data-sets.html
if __name__ == '__main__':
    """
	create-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-data-set.html
	delete-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-data-set.html
	get-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-data-set.html
	update-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-data-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("dataexchange", "list-data-sets", add_option_dict)