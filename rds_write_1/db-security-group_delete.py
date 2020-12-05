#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-security-group.html
if __name__ == '__main__':
    """
	create-db-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-security-group.html
	describe-db-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-security-groups.html
    """

    parameter_display_string = """
    # db-security-group-name : The name of the DB security group to delete.

Note
You canât delete the default DB security group.

Constraints:

Must be 1 to 255 letters, numbers, or hyphens.
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens
Must not be âDefaultâ
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "delete-db-security-group", "db-security-group-name", add_option_dict)





