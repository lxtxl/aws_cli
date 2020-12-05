#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/copy-db-cluster-snapshot.html
if __name__ == '__main__':
    """
	create-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-cluster-snapshot.html
	delete-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster-snapshot.html
	describe-db-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-cluster-snapshots.html
    """

    parameter_display_string = """
    # source-db-cluster-snapshot-identifier : The identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive.
You canât copy from one AWS Region to another.
Constraints:

Must specify a valid system snapshot in the âavailableâ state.
Specify a valid DB snapshot identifier.

Example: my-cluster-snapshot1
    # target-db-cluster-snapshot-identifier : The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: my-cluster-snapshot2
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("neptune", "copy-db-cluster-snapshot", "source-db-cluster-snapshot-identifier", "target-db-cluster-snapshot-identifier", add_option_dict)
