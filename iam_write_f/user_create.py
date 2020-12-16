#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user.html
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html
	tag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-user.html
	untag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-user.html
    """

    write_parameter("iam", "create-user")