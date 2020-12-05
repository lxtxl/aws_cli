#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster.html
if __name__ == '__main__':
    """
	backtrack-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/backtrack-db-cluster.html
	delete-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster.html
	describe-db-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-clusters.html
	failover-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/failover-db-cluster.html
	modify-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster.html
	start-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-cluster.html
	stop-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-cluster.html
    """

    parameter_display_string = """
    # db-cluster-identifier : The DB cluster identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
First character must be a letter.
Canât end with a hyphen or contain two consecutive hyphens.

Example: my-cluster1
    # engine : The name of the database engine to be used for this DB cluster.
Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "create-db-cluster", "db-cluster-identifier", "engine", add_option_dict)
