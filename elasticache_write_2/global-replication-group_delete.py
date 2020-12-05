#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-global-replication-group.html
if __name__ == '__main__':
    """
	create-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-global-replication-group.html
	describe-global-replication-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-global-replication-groups.html
	disassociate-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/disassociate-global-replication-group.html
	failover-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/failover-global-replication-group.html
	modify-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-global-replication-group.html
    """

    parameter_display_string = """
    # global-replication-group-id : The name of the Global Datastore
    # retain-primary-replication-group | --no-retain-primary-replication-group : The primary replication group is retained as a standalone replication group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "delete-global-replication-group", "global-replication-group-id", "retain-primary-replication-group | --no-retain-primary-replication-group", add_option_dict)
