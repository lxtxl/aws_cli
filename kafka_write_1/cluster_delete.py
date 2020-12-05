#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/delete-cluster.html
if __name__ == '__main__':
    """
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-cluster.html
	describe-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-clusters.html
    """

    parameter_display_string = """
    # cluster-arn : The Amazon Resource Name (ARN) that uniquely identifies the cluster.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kafka", "delete-cluster", "cluster-arn", add_option_dict)





