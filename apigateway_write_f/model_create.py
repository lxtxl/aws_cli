#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-model.html
	get-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-model.html
	get-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-models.html
	update-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-model.html
    """

    write_parameter("apigateway", "create-model")