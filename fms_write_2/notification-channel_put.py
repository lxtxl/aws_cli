#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-notification-channel.html
if __name__ == '__main__':
    """
	delete-notification-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-notification-channel.html
	get-notification-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-notification-channel.html
    """

    parameter_display_string = """
    # sns-topic-arn : The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager.
    # sns-role-name : The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("fms", "put-notification-channel", "sns-topic-arn", "sns-role-name", add_option_dict)
