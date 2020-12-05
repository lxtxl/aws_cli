#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-cluster.html
if __name__ == '__main__':
    """
	delete-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-cluster.html
	describe-cache-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-clusters.html
	modify-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-cluster.html
	reboot-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/reboot-cache-cluster.html
    """

    parameter_display_string = """
    # cache-cluster-id : The node group (shard) identifier. This parameter is stored as a lowercase string.

Constraints:


A name must contain from 1 to 50 alphanumeric characters or hyphens.
The first character must be a letter.
A name cannot end with a hyphen or contain two consecutive hyphens.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "create-cache-cluster", "cache-cluster-id", add_option_dict)





