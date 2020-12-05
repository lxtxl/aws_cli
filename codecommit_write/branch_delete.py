#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-branch.html
	get-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-branch.html
	list-branches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-branches.html
    """

    write_parameter("codecommit", "delete-branch")