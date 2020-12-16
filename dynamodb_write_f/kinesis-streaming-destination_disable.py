#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-kinesis-streaming-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-kinesis-streaming-destination.html
	enable-kinesis-streaming-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/enable-kinesis-streaming-destination.html
    """

    write_parameter("dynamodb", "disable-kinesis-streaming-destination")