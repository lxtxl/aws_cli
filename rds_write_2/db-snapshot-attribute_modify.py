#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot-attribute.html
if __name__ == '__main__':
    """
	describe-db-snapshot-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshot-attributes.html
    """

    parameter_display_string = """
    # db-snapshot-identifier : The identifier for the DB snapshot to modify the attributes for.
    # attribute-name : The name of the DB snapshot attribute to modify.
To manage authorization for other AWS accounts to copy or restore a manual DB snapshot, set this value to restore .

Note
To view the list of attributes available to modify, use the  DescribeDBSnapshotAttributes API action.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "modify-db-snapshot-attribute", "db-snapshot-identifier", "attribute-name", add_option_dict)
