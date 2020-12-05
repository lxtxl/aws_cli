#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-cluster-to-point-in-time.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-cluster-identifier : The name of the new DB cluster to be created.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens
    # source-db-cluster-identifier : The identifier of the source DB cluster from which to restore.
Constraints:

Must match the identifier of an existing DBCluster.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "restore-db-cluster-to-point-in-time", "db-cluster-identifier", "source-db-cluster-identifier", add_option_dict)
