#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/batch-modify-cluster-snapshots.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # snapshot-identifier-list : A list of snapshot identifiers you want to modify.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "batch-modify-cluster-snapshots", "snapshot-identifier-list", add_option_dict)





