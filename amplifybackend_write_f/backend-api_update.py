#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-backend-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-backend-api.html
	delete-backend-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/delete-backend-api.html
	get-backend-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/get-backend-api.html
    """

    write_parameter("amplifybackend", "update-backend-api")