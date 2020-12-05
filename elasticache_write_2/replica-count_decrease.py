#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/decrease-replica-count.html
if __name__ == '__main__':
    """
	increase-replica-count : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/increase-replica-count.html
    """

    parameter_display_string = """
    # replication-group-id : The id of the replication group from which you want to remove replica nodes.
    # apply-immediately | --no-apply-immediately : If True , the number of replica nodes is decreased immediately. ApplyImmediately=False is not currently supported.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "decrease-replica-count", "replication-group-id", "apply-immediately | --no-apply-immediately", add_option_dict)
