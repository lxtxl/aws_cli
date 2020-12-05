#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-parameter-group.html
if __name__ == '__main__':
    """
	copy-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-parameter-group.html
	create-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-parameter-group.html
	delete-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-parameter-group.html
	describe-db-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-parameter-groups.html
	modify-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-parameter-group.html
    """

    parameter_display_string = """
    # db-parameter-group-name : The name of the DB parameter group.
Constraints:

Must match the name of an existing DBParameterGroup .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "reset-db-parameter-group", "db-parameter-group-name", add_option_dict)





