#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-cluster-snapshot-attribute.html
if __name__ == '__main__':
    """
	describe-db-cluster-snapshot-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-cluster-snapshot-attributes.html
    """

    parameter_display_string = """
    # db-cluster-snapshot-identifier : The identifier for the DB cluster snapshot to modify the attributes for.
    # attribute-name : The name of the DB cluster snapshot attribute to modify.
To manage authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this value to restore .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("neptune", "modify-db-cluster-snapshot-attribute", "db-cluster-snapshot-identifier", "attribute-name", add_option_dict)
