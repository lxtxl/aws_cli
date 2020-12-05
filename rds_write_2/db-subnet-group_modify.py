#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-subnet-group.html
if __name__ == '__main__':
    """
	create-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-subnet-group.html
	delete-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-subnet-group.html
	describe-db-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-subnet-groups.html
    """

    parameter_display_string = """
    # db-subnet-group-name : The name for the DB subnet group. This value is stored as a lowercase string. You canât modify the default subnet group.
Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
Example: mySubnetgroup
    # subnet-ids : The EC2 subnet IDs for the DB subnet group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "modify-db-subnet-group", "db-subnet-group-name", "subnet-ids", add_option_dict)
