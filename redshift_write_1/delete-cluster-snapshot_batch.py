#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/batch-delete-cluster-snapshots.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # identifiers : A list of identifiers for the snapshots that you want to delete.
(structure)

SnapshotIdentifier -> (string)

The unique identifier of the manual snapshot to be deleted.
Constraints: Must be the name of an existing snapshot that is in the available , failed , or cancelled state.

SnapshotClusterIdentifier -> (string)

The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
Constraints: Must be the name of valid cluster.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "batch-delete-cluster-snapshots", "identifiers", add_option_dict)





