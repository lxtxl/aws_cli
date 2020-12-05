#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/register-stream-consumer.html
if __name__ == '__main__':
    """
	deregister-stream-consumer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/deregister-stream-consumer.html
	describe-stream-consumer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream-consumer.html
	list-stream-consumers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-stream-consumers.html
    """

    parameter_display_string = """
    # stream-arn : The ARN of the Kinesis data stream that you want to register the consumer with. For more info, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    # consumer-name : For a given Kinesis data stream, each consumer must have a unique name. However, consumer names donât have to be unique across data streams.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesis", "register-stream-consumer", "stream-arn", "consumer-name", add_option_dict)
