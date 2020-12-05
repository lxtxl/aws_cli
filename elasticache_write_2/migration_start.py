#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/start-migration.html
if __name__ == '__main__':
    """
	complete-migration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/complete-migration.html
    """

    parameter_display_string = """
    # replication-group-id : The ID of the replication group to which data should be migrated.
    # customer-node-endpoint-list : List of endpoints from which data should be migrated. For Redis (cluster mode disabled), list should have only one element.
(structure)

The endpoint from which data should be migrated.
Address -> (string)

The address of the node endpoint

Port -> (integer)

The port of the node endpoint
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "start-migration", "replication-group-id", "customer-node-endpoint-list", add_option_dict)
