#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster-snapshot.html
if __name__ == '__main__':
    """
	copy-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-snapshot.html
	create-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster-snapshot.html
	describe-db-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-snapshots.html
    """

    parameter_display_string = """
    # db-cluster-snapshot-identifier : The identifier of the cluster snapshot to delete.
Constraints: Must be the name of an existing cluster snapshot in the available state.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("docdb", "delete-db-cluster-snapshot", "db-cluster-snapshot-identifier", add_option_dict)





