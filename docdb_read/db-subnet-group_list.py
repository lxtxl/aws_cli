#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-subnet-groups.html
if __name__ == '__main__':
    """
	create-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-subnet-group.html
	delete-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-subnet-group.html
	modify-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-subnet-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("docdb", "describe-db-subnet-groups", add_option_dict)