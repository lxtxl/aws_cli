#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-parameter-group.html
if __name__ == '__main__':
    """
	copy-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-parameter-group.html
	delete-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-parameter-group.html
	describe-db-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-parameter-groups.html
	modify-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-parameter-group.html
	reset-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-parameter-group.html
    """

    parameter_display_string = """
    # db-parameter-group-name : The name of the DB parameter group.
Constraints:

Must be 1 to 255 letters, numbers, or hyphens.
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens


Note
This value is stored as a lowercase string.
    # db-parameter-group-family : The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.
To list all of the available parameter group families, use the following command:

aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily"


Note
The output contains duplicates.
    # description : The description for the DB parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "create-db-parameter-group", "db-parameter-group-name", "db-parameter-group-family", "description", add_option_dict)
