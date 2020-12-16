#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodbstreams/get-shard-iterator.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # stream-arn : The Amazon Resource Name (ARN) for the stream.
    # shard-id : The identifier of the shard. The iterator will be returned for this shard ID.
    """

    execute_two_parameter("dynamodbstreams", "get-shard-iterator", "stream-arn", "shard-id", parameter_display_string)