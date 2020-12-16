#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-data-sync.html
if __name__ == '__main__':
    """
	create-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-resource-data-sync.html
	delete-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-resource-data-sync.html
	update-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-resource-data-sync.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ssm", "list-resource-data-sync", add_option_dict)