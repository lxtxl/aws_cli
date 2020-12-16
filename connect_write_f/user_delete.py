#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user.html
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-users.html
    """

    write_parameter("connect", "delete-user")