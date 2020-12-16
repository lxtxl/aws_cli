#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/put.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-id : Cluster Id of cluster you want to put file onto
    # key-pair-file : Private key file to use for login
    # src : Source file path on local machine
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("emr", "put", "cluster-id", "key-pair-file", "src", add_option_dict)
