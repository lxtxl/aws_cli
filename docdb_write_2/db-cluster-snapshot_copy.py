#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-snapshot.html
if __name__ == '__main__':
    """
	create-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster-snapshot.html
	delete-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster-snapshot.html
	describe-db-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-snapshots.html
    """

    parameter_display_string = """
    # source-db-cluster-snapshot-identifier : The identifier of the cluster snapshot to copy. This parameter is not case sensitive.
Constraints:

Must specify a valid system snapshot in the available state.
If the source snapshot is in the same AWS Region as the copy, specify a valid snapshot identifier.
If the source snapshot is in a different AWS Region than the copy, specify a valid cluster snapshot ARN.

Example: my-cluster-snapshot1
    # target-db-cluster-snapshot-identifier : The identifier of the new cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
The first character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: my-cluster-snapshot2
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("docdb", "copy-db-cluster-snapshot", "source-db-cluster-snapshot-identifier", "target-db-cluster-snapshot-identifier", add_option_dict)
