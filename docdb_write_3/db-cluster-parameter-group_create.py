#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster-parameter-group.html
if __name__ == '__main__':
    """
	copy-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-parameter-group.html
	delete-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster-parameter-group.html
	describe-db-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-parameter-groups.html
	modify-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster-parameter-group.html
	reset-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/reset-db-cluster-parameter-group.html
    """

    parameter_display_string = """
    # db-cluster-parameter-group-name : The name of the cluster parameter group.
Constraints:

Must not match the name of an existing DBClusterParameterGroup .


Note
This value is stored as a lowercase string.
    # db-parameter-group-family : The cluster parameter group family name.
    # description : The description for the cluster parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("docdb", "create-db-cluster-parameter-group", "db-cluster-parameter-group-name", "db-parameter-group-family", "description", add_option_dict)
