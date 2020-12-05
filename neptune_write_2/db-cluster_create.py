#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-cluster.html
if __name__ == '__main__':
    """
	delete-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster.html
	describe-db-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-clusters.html
	failover-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/failover-db-cluster.html
	modify-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-cluster.html
	start-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/start-db-cluster.html
	stop-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/stop-db-cluster.html
    """

    parameter_display_string = """
    # db-cluster-identifier : The DB cluster identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: my-cluster1
    # engine : The name of the database engine to be used for this DB cluster.
Valid Values: neptune
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("neptune", "create-db-cluster", "db-cluster-identifier", "engine", add_option_dict)
