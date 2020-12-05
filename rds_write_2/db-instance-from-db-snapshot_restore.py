#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-instance-from-db-snapshot.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-instance-identifier : Name of the DB instance to create from the DB snapshot. This parameter isnât case-sensitive.
Constraints:

Must contain from 1 to 63 numbers, letters, or hyphens
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens

Example: my-snapshot-id
    # db-snapshot-identifier : The identifier for the DB snapshot to restore from.
Constraints:

Must match the identifier of an existing DBSnapshot.
If you are restoring from a shared manual DB snapshot, the DBSnapshotIdentifier must be the ARN of the shared DB snapshot.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "restore-db-instance-from-db-snapshot", "db-instance-identifier", "db-snapshot-identifier", add_option_dict)
