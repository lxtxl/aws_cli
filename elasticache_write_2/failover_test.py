#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/test-failover.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # replication-group-id : The name of the replication group (console: cluster) whose automatic failover is being tested by this operation.
    # node-group-id : The name of the node group (called shard in the console) in this replication group on which automatic failover is to be tested. You may test automatic failover on up to 5 node groups in any rolling 24-hour period.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "test-failover", "replication-group-id", "node-group-id", add_option_dict)
