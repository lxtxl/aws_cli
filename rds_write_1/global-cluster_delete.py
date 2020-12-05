#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-global-cluster.html
if __name__ == '__main__':
    """
	create-global-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-global-cluster.html
	describe-global-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-global-clusters.html
	modify-global-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-global-cluster.html
    """

    parameter_display_string = """
    # global-cluster-identifier : The cluster identifier of the global database cluster being deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "delete-global-cluster", "global-cluster-identifier", add_option_dict)





