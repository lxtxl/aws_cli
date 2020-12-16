#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-notification-configuration.html
if __name__ == '__main__':
    """
	delete-notification-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-notification-configuration.html
	describe-notification-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-notification-configurations.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # topic-arn : The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS) topic.
    # notification-types : The type of event that causes the notification to be sent. To query the notification types supported by Amazon EC2 Auto Scaling, call the  DescribeAutoScalingNotificationTypes API.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("autoscaling", "put-notification-configuration", "auto-scaling-group-name", "topic-arn", "notification-types", add_option_dict)
