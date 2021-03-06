#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-ecs-cluster.html
if __name__ == '__main__':
    """
	describe-ecs-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-ecs-clusters.html
	register-ecs-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-ecs-cluster.html
    """

    parameter_display_string = """
    # ecs-cluster-arn : The clusterâs Amazon Resource Number (ARN).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("opsworks", "deregister-ecs-cluster", "ecs-cluster-arn", add_option_dict)





