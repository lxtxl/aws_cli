#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/disassociate-global-replication-group.html
if __name__ == '__main__':
    """
	create-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-global-replication-group.html
	delete-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-global-replication-group.html
	describe-global-replication-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-global-replication-groups.html
	failover-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/failover-global-replication-group.html
	modify-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-global-replication-group.html
    """

    parameter_display_string = """
    # global-replication-group-id : The name of the Global Datastore
    # replication-group-id : The name of the secondary cluster you wish to remove from the Global Datastore
    # replication-group-region : The AWS region of secondary cluster you wish to remove from the Global Datastore
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("elasticache", "disassociate-global-replication-group", "global-replication-group-id", "replication-group-id", "replication-group-region", add_option_dict)
