#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/rebalance-slots-in-global-replication-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # global-replication-group-id : The name of the Global Datastore
    # apply-immediately | --no-apply-immediately : If True , redistribution is applied immediately.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "rebalance-slots-in-global-replication-group", "global-replication-group-id", "apply-immediately | --no-apply-immediately", add_option_dict)
