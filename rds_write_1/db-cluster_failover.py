#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/failover-db-cluster.html
if __name__ == '__main__':
    """
	backtrack-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/backtrack-db-cluster.html
	create-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster.html
	delete-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster.html
	describe-db-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-clusters.html
	modify-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster.html
	start-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-cluster.html
	stop-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-cluster.html
    """

    parameter_display_string = """
    # db-cluster-identifier : A DB cluster identifier to force a failover for. This parameter isnât case-sensitive.
Constraints:

Must match the identifier of an existing DBCluster.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "failover-db-cluster", "db-cluster-identifier", add_option_dict)





