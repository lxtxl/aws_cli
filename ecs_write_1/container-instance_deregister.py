#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deregister-container-instance.html
if __name__ == '__main__':
    """
	describe-container-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-container-instances.html
	list-container-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-container-instances.html
	register-container-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-container-instance.html
    """

    parameter_display_string = """
    # container-instance : The container instance ID or full ARN of the container instance to deregister. The ARN contains the arn:aws:ecs namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the container-instance namespace, and then the container instance ID. For example, arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "deregister-container-instance", "container-instance", add_option_dict)





