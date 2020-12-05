#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-notification-configuration.html
if __name__ == '__main__':
    """
	describe-notification-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-notification-configurations.html
	put-notification-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-notification-configuration.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # topic-arn : The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS) topic.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "delete-notification-configuration", "auto-scaling-group-name", "topic-arn", add_option_dict)
