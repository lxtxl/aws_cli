#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-snapshot.html
if __name__ == '__main__':
    """
	create-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-snapshot.html
	delete-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-snapshot.html
	describe-db-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshots.html
	modify-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot.html
    """

    parameter_display_string = """
    # source-db-snapshot-identifier : The identifier for the source DB snapshot.
If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier. For example, you might specify rds:mysql-instance1-snapshot-20130805 .
If the source snapshot is in a different AWS Region than the copy, specify a valid DB snapshot ARN. For example, you might specify arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805 .
If you are copying from a shared manual DB snapshot, this parameter must be the Amazon Resource Name (ARN) of the shared DB snapshot.
If you are copying an encrypted snapshot this parameter must be in the ARN format for the source AWS Region, and must match the SourceDBSnapshotIdentifier in the PreSignedUrl parameter.
Constraints:

Must specify a valid system snapshot in the âavailableâ state.

Example: rds:mydb-2012-04-02-00-01
Example: arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805
    # target-db-snapshot-identifier : The identifier for the copy of the snapshot.
Constraints:

Canât be null, empty, or blank
Must contain from 1 to 255 letters, numbers, or hyphens
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens

Example: my-db-snapshot
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "copy-db-snapshot", "source-db-snapshot-identifier", "target-db-snapshot-identifier", add_option_dict)
