#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-subnet-group.html
if __name__ == '__main__':
    """
	create-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-subnet-group.html
	describe-db-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-subnet-groups.html
	modify-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-subnet-group.html
    """

    parameter_display_string = """
    # db-subnet-group-name : The name of the database subnet group to delete.

Note
You canât delete the default subnet group.

Constraints:
Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
Example: mySubnetgroup
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "delete-db-subnet-group", "db-subnet-group-name", add_option_dict)





