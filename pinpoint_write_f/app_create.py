#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-app.html
	get-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-app.html
	get-apps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-apps.html
    """

    write_parameter("pinpoint", "create-app")