#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-replication-group-shard-configuration.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # replication-group-id : The name of the Redis (cluster mode enabled) cluster (replication group) on which the shards are to be configured.
    # node-group-count : The number of node groups (shards) that results from the modification of the shard configuration.
    # apply-immediately | --no-apply-immediately : Indicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is true .
Value: true
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("elasticache", "modify-replication-group-shard-configuration", "replication-group-id", "node-group-count", "apply-immediately | --no-apply-immediately", add_option_dict)
