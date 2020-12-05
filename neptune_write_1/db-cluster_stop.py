#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/stop-db-cluster.html
if __name__ == '__main__':
    """
	create-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-cluster.html
	delete-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster.html
	describe-db-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-clusters.html
	failover-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/failover-db-cluster.html
	modify-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-cluster.html
	start-db-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/start-db-cluster.html
    """

    parameter_display_string = """
    # db-cluster-identifier : The DB cluster identifier of the Neptune DB cluster to be stopped. This parameter is stored as a lowercase string.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("neptune", "stop-db-cluster", "db-cluster-identifier", add_option_dict)





