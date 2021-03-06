#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-pull-request : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request.html
	list-pull-requests : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-pull-requests.html
    """

    write_parameter("codecommit", "create-pull-request")