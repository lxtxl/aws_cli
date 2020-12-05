#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-global-replication-group.html
if __name__ == '__main__':
    """
	delete-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-global-replication-group.html
	describe-global-replication-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-global-replication-groups.html
	disassociate-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/disassociate-global-replication-group.html
	failover-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/failover-global-replication-group.html
	modify-global-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-global-replication-group.html
    """

    parameter_display_string = """
    # global-replication-group-id-suffix : The suffix name of a Global Datastore. Amazon ElastiCache automatically applies a prefix to the Global Datastore ID when it is created. Each AWS Region has its own prefix. For instance, a Global Datastore ID created in the US-West-1 region will begin with âdsdfuâ along with the suffix name you provide. The suffix, combined with the auto-generated prefix, guarantees uniqueness of the Global Datastore name across multiple regions.
For a full list of AWS Regions and their respective Global Datastore iD prefixes, see Using the AWS CLI with Global Datastores .
    # primary-replication-group-id : The name of the primary cluster that accepts writes and will replicate updates to the secondary cluster.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "create-global-replication-group", "global-replication-group-id-suffix", "primary-replication-group-id", add_option_dict)
