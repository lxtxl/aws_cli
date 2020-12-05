#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-global-replication-groups.html
if __name__ == '__main__':
    """
	create-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-global-replication-group.html
	delete-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-global-replication-group.html
	disassociate-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/disassociate-global-replication-group.html
	failover-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/failover-global-replication-group.html
	modify-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-global-replication-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("elasticache", "describe-global-replication-groups", add_option_dict)