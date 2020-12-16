#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-destination.html
if __name__ == '__main__':
    """
	delete-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-destination.html
	describe-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-destinations.html
    """

    parameter_display_string = """
    # destination-name : A name for the destination.
    # target-arn : The ARN of an Amazon Kinesis stream to which to deliver matching log events.
    # role-arn : The ARN of an IAM role that grants CloudWatch Logs permissions to call the Amazon Kinesis PutRecord operation on the destination stream.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("logs", "put-destination", "destination-name", "target-arn", "role-arn", add_option_dict)
