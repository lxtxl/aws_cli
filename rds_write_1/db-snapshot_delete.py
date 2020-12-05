#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-snapshot.html
if __name__ == '__main__':
    """
	copy-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-snapshot.html
	create-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-snapshot.html
	describe-db-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshots.html
	modify-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot.html
    """

    parameter_display_string = """
    # db-snapshot-identifier : The DB snapshot identifier.
Constraints: Must be the name of an existing DB snapshot in the available state.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "delete-db-snapshot", "db-snapshot-identifier", add_option_dict)





