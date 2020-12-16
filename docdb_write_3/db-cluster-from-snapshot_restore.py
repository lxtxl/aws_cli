#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/restore-db-cluster-from-snapshot.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-cluster-identifier : The name of the cluster to create from the snapshot or cluster snapshot. This parameter isnât case sensitive.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
The first character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: my-snapshot-id
    # snapshot-identifier : The identifier for the snapshot or cluster snapshot to restore from.
You can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot.
Constraints:

Must match the identifier of an existing snapshot.
    # engine : The database engine to use for the new cluster.
Default: The same as source.
Constraint: Must be compatible with the engine of the source.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("docdb", "restore-db-cluster-from-snapshot", "db-cluster-identifier", "snapshot-identifier", "engine", add_option_dict)
