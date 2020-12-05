#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-parameter-groups.html
if __name__ == '__main__':
    """
	copy-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-parameter-group.html
	create-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster-parameter-group.html
	delete-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster-parameter-group.html
	modify-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster-parameter-group.html
	reset-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/reset-db-cluster-parameter-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("docdb", "describe-db-cluster-parameter-groups", add_option_dict)