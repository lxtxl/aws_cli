#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-message.html
	receive-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html
    """

    write_parameter("sqs", "send-message")