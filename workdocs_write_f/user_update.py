#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	activate-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/activate-user.html
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-user.html
	deactivate-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/deactivate-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-user.html
	describe-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-users.html
    """

    write_parameter("workdocs", "update-user")