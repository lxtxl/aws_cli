#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-app-instance-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-app-instance-user.html
	describe-app-instance-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-app-instance-user.html
	list-app-instance-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-app-instance-users.html
	update-app-instance-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-app-instance-user.html
    """

    write_parameter("chime", "delete-app-instance-user")