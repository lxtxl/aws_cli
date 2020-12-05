#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/reboot-cache-cluster.html
if __name__ == '__main__':
    """
	create-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-cluster.html
	delete-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-cluster.html
	describe-cache-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-clusters.html
	modify-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-cluster.html
    """

    parameter_display_string = """
    # cache-cluster-id : The cluster identifier. This parameter is stored as a lowercase string.
    # cache-node-ids-to-reboot : A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cluster, specify all of the cache node IDs.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "reboot-cache-cluster", "cache-cluster-id", "cache-node-ids-to-reboot", add_option_dict)
