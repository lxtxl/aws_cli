#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-snapshot.html
if __name__ == '__main__':
    """
	copy-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-snapshot.html
	delete-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-snapshot.html
	describe-db-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshots.html
	modify-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot.html
    """

    parameter_display_string = """
    # db-snapshot-identifier : The identifier for the DB snapshot.
Constraints:

Canât be null, empty, or blank
Must contain from 1 to 255 letters, numbers, or hyphens
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens

Example: my-snapshot-id
    # db-instance-identifier : The identifier of the DB instance that you want to create the snapshot of.
Constraints:

Must match the identifier of an existing DBInstance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "create-db-snapshot", "db-snapshot-identifier", "db-instance-identifier", add_option_dict)
