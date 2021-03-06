#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-replication-group.html
if __name__ == '__main__':
    """
	create-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-replication-group.html
	delete-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-replication-group.html
	describe-replication-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-replication-groups.html
    """

    parameter_display_string = """
    # replication-group-id : The identifier of the replication group to modify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "modify-replication-group", "replication-group-id", add_option_dict)





