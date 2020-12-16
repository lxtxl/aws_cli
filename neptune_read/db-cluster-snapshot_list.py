#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-cluster-snapshots.html
if __name__ == '__main__':
    """
	copy-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/copy-db-cluster-snapshot.html
	create-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-cluster-snapshot.html
	delete-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster-snapshot.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("neptune", "describe-db-cluster-snapshots", add_option_dict)