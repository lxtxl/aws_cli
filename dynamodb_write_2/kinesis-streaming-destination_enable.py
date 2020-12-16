#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/enable-kinesis-streaming-destination.html
if __name__ == '__main__':
    """
	describe-kinesis-streaming-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-kinesis-streaming-destination.html
	disable-kinesis-streaming-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/disable-kinesis-streaming-destination.html
    """

    parameter_display_string = """
    # table-name : The name of the DynamoDB table.
    # stream-arn : The ARN for a Kinesis data stream.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "enable-kinesis-streaming-destination", "table-name", "stream-arn", add_option_dict)
