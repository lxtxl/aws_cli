#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-cluster.html
if __name__ == '__main__':
    """
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-cluster.html
	describe-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-clusters.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-clusters.html
    """

    parameter_display_string = """
    # cluster : The short name or full Amazon Resource Name (ARN) of the cluster to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "delete-cluster", "cluster", add_option_dict)





