#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-replication-group.html
if __name__ == '__main__':
    """
	delete-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-replication-group.html
	describe-replication-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-replication-groups.html
	modify-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-replication-group.html
    """

    parameter_display_string = """
    # replication-group-id : The replication group identifier. This parameter is stored as a lowercase string.
Constraints:

A name must contain from 1 to 40 alphanumeric characters or hyphens.
The first character must be a letter.
A name cannot end with a hyphen or contain two consecutive hyphens.
    # replication-group-description : A user-created description for the replication group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "create-replication-group", "replication-group-id", "replication-group-description", add_option_dict)
