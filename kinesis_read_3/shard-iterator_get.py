#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-shard-iterator.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # stream-name : The name of the Amazon Kinesis data stream.
    # shard-id : The shard ID of the Kinesis Data Streams shard to get the iterator for.
    """

    execute_two_parameter("kinesis", "get-shard-iterator", "stream-name", "shard-id", parameter_display_string)