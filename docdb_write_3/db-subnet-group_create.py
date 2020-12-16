#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-subnet-group.html
if __name__ == '__main__':
    """
	delete-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-subnet-group.html
	describe-db-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-subnet-groups.html
	modify-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-subnet-group.html
    """

    parameter_display_string = """
    # db-subnet-group-name : The name for the subnet group. This value is stored as a lowercase string.
Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.
Example: mySubnetgroup
    # db-subnet-group-description : The description for the subnet group.
    # subnet-ids : The Amazon EC2 subnet IDs for the subnet group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("docdb", "create-db-subnet-group", "db-subnet-group-name", "db-subnet-group-description", "subnet-ids", add_option_dict)
