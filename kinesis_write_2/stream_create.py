#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/create-stream.html
if __name__ == '__main__':
    """
	delete-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/delete-stream.html
	describe-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream.html
	list-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-streams.html
    """

    parameter_display_string = """
    # stream-name : A name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by AWS Region. That is, two streams in two different AWS accounts can have the same name. Two streams in the same AWS account but in two different Regions can also have the same name.
    # shard-count : The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesis", "create-stream", "stream-name", "shard-count", add_option_dict)
