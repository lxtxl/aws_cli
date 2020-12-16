#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-cluster-configuration.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-arn : The Amazon Resource Name (ARN) that uniquely identifies the cluster.
    # configuration-info : 
    # current-version : The version of the cluster that needs to be updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kafka", "update-cluster-configuration", "cluster-arn", "configuration-info", "current-version", add_option_dict)
