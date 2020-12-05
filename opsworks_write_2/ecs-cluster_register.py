#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-ecs-cluster.html
if __name__ == '__main__':
    """
	deregister-ecs-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-ecs-cluster.html
	describe-ecs-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-ecs-clusters.html
    """

    parameter_display_string = """
    # ecs-cluster-arn : The clusterâs ARN.
    # stack-id : The stack ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks", "register-ecs-cluster", "ecs-cluster-arn", "stack-id", add_option_dict)
