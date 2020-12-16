#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-broker-count.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-arn : The Amazon Resource Name (ARN) that uniquely identifies the cluster.
    # current-version : The version of cluster to update from. A successful operation will then generate a new version.
    # target-number-of-broker-nodes : The number of broker nodes that you want the cluster to have after this operation completes successfully.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kafka", "update-broker-count", "cluster-arn", "current-version", "target-number-of-broker-nodes", add_option_dict)
