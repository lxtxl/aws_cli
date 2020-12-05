#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-backtracks.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-cluster-identifier : The DB cluster identifier of the DB cluster to be described. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 alphanumeric characters or hyphens.
First character must be a letter.
Canât end with a hyphen or contain two consecutive hyphens.

Example: my-cluster1
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("rds", "describe-db-cluster-backtracks", "db-cluster-identifier", add_option_dict)