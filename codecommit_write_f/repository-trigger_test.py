#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-repository-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-repository-triggers.html
	put-repository-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-repository-triggers.html
    """

    write_parameter("codecommit", "test-repository-triggers")