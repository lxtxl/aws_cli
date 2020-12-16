#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshots.html
if __name__ == '__main__':
    """
	copy-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-snapshot.html
	create-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-snapshot.html
	delete-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-snapshot.html
	modify-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("rds", "describe-db-snapshots", add_option_dict)