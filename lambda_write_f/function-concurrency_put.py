#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-function-concurrency : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-concurrency.html
	get-function-concurrency : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-concurrency.html
    """

    write_parameter("lambda", "put-function-concurrency")