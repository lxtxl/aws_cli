#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-api-key.html
	get-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-key.html
	get-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-keys.html
	import-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-api-keys.html
	update-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-api-key.html
    """

    write_parameter("apigateway", "delete-api-key")