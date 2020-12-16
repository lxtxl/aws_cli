#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-group.html
	describe-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-groups.html
    """

    write_parameter("workmail", "create-group")