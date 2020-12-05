#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-cluster-snapshot.html
if __name__ == '__main__':
    """
	create-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-snapshot.html
	delete-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-snapshot.html
	describe-db-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-snapshots.html
    """

    parameter_display_string = """
    # source-db-cluster-snapshot-identifier : The identifier of the DB cluster snapshot to copy. This parameter isnât case-sensitive.
You canât copy an encrypted, shared DB cluster snapshot from one AWS Region to another.
Constraints:

Must specify a valid system snapshot in the âavailableâ state.
If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier.
If the source snapshot is in a different AWS Region than the copy, specify a valid DB cluster snapshot ARN. For more information, go to Copying Snapshots Across AWS Regions in the Amazon Aurora User Guide.

Example: my-cluster-snapshot1
    # target-db-cluster-snapshot-identifier : The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter isnât case-sensitive.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
First character must be a letter.
Canât end with a hyphen or contain two consecutive hyphens.

Example: my-cluster-snapshot2
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "copy-db-cluster-snapshot", "source-db-cluster-snapshot-identifier", "target-db-cluster-snapshot-identifier", add_option_dict)
