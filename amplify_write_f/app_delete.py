#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-app.html
	get-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-app.html
	list-apps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-apps.html
	update-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/update-app.html
    """

    write_parameter("amplify", "delete-app")