#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-clusters.html
if __name__ == '__main__':
    """
	backtrack-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/backtrack-db-cluster.html
	create-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster.html
	delete-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster.html
	failover-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/failover-db-cluster.html
	modify-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster.html
	start-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-cluster.html
	stop-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-cluster.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("rds", "describe-db-clusters", add_option_dict)