#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-from-cluster-snapshot.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-identifier : The identifier of the cluster that will be created from restoring the snapshot.
Constraints:

Must contain from 1 to 63 alphanumeric characters or hyphens.
Alphabetic characters must be lowercase.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.
Must be unique for all clusters within an AWS account.
    # snapshot-identifier : The name of the snapshot from which to create the new cluster. This parameter isnât case sensitive.
Example: my-snapshot-id
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "restore-from-cluster-snapshot", "cluster-identifier", "snapshot-identifier", add_option_dict)
