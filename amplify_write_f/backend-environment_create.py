#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-backend-environment.html
	get-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-backend-environment.html
	list-backend-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-backend-environments.html
    """

    write_parameter("amplify", "create-backend-environment")