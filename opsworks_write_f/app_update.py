#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-app.html
	delete-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-app.html
	describe-apps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-apps.html
    """

    write_parameter("opsworks", "update-app")