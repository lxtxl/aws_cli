#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-stream-consumer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/deregister-stream-consumer.html
	describe-stream-consumer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream-consumer.html
	list-stream-consumers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-stream-consumers.html
    """

    write_parameter("kinesis", "register-stream-consumer")