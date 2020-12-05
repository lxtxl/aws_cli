#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/delete-members.html
	get-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/get-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-members.html
    """

    write_parameter("detective", "create-members")