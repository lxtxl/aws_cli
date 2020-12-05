#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-global-table.html
if __name__ == '__main__':
    """
	create-global-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-global-table.html
	describe-global-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table.html
	list-global-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-global-tables.html
    """

    parameter_display_string = """
    # global-table-name : The global table name.
    # replica-updates : A list of Regions that should be added or removed from the global table.
(structure)

Represents one of the following:

A new replica to be added to an existing global table.
New parameters for an existing replica.
An existing replica to be removed from an existing global table.

Create -> (structure)

The parameters required for creating a replica on an existing global table.
RegionName -> (string)

The Region of the replica to be added.


Delete -> (structure)

The name of the existing replica to be removed.
RegionName -> (string)

The Region of the replica to be removed.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "update-global-table", "global-table-name", "replica-updates", add_option_dict)
