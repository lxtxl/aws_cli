#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-users.html
	register-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/register-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-user.html
    """

    write_parameter("quicksight", "delete-user")