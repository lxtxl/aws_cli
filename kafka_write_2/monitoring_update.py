#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-monitoring.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-arn : The Amazon Resource Name (ARN) that uniquely identifies the cluster.
    # current-version : The version of the MSK cluster to update. Cluster versions arenât simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kafka", "update-monitoring", "cluster-arn", "current-version", add_option_dict)
