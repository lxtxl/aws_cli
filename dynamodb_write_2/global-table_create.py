#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-global-table.html
if __name__ == '__main__':
    """
	describe-global-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table.html
	list-global-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-global-tables.html
	update-global-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-global-table.html
    """

    parameter_display_string = """
    # global-table-name : The global table name.
    # replication-group : The Regions where the global table needs to be created.
(structure)

Represents the properties of a replica.
RegionName -> (string)

The Region where the replica needs to be created.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "create-global-table", "global-table-name", "replication-group", add_option_dict)
