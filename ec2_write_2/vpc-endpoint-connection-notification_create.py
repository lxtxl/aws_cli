#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint-connection-notification.html
if __name__ == '__main__':
    """
	delete-vpc-endpoint-connection-notifications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoint-connection-notifications.html
	describe-vpc-endpoint-connection-notifications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-connection-notifications.html
	modify-vpc-endpoint-connection-notification : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint-connection-notification.html
    """

    parameter_display_string = """
    # connection-notification-arn : The ARN of the SNS topic for the notifications.
    # connection-events : One or more endpoint events for which to receive notifications. Valid values are Accept , Connect , Delete , and Reject .
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-vpc-endpoint-connection-notification", "connection-notification-arn", "connection-events", add_option_dict)
