#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-cluster-snapshot.html
if __name__ == '__main__':
    """
	copy-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/copy-db-cluster-snapshot.html
	delete-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster-snapshot.html
	describe-db-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-cluster-snapshots.html
    """

    parameter_display_string = """
    # db-cluster-snapshot-identifier : The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: my-cluster1-snapshot1
    # db-cluster-identifier : The identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.
Constraints:

Must match the identifier of an existing DBCluster.

Example: my-cluster1
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("neptune", "create-db-cluster-snapshot", "db-cluster-snapshot-identifier", "db-cluster-identifier", add_option_dict)
