#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-parameter-group.html
if __name__ == '__main__':
    """
	copy-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-cluster-parameter-group.html
	delete-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-parameter-group.html
	describe-db-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-parameter-groups.html
	modify-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-parameter-group.html
	reset-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-cluster-parameter-group.html
    """

    parameter_display_string = """
    # db-cluster-parameter-group-name : The name of the DB cluster parameter group.
Constraints:

Must match the name of an existing DB cluster parameter group.


Note
This value is stored as a lowercase string.
    # db-parameter-group-family : The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.

Aurora MySQL

Example: aurora5.6 , aurora-mysql5.7

Aurora PostgreSQL

Example: aurora-postgresql9.6
    # description : The description for the DB cluster parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "create-db-cluster-parameter-group", "db-cluster-parameter-group-name", "db-parameter-group-family", "description", add_option_dict)
