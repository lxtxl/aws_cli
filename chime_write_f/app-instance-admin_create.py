#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-app-instance-admin : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance-admin.html
	describe-app-instance-admin : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-app-instance-admin.html
	list-app-instance-admins : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-app-instance-admins.html
    """

    write_parameter("chime", "create-app-instance-admin")