#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-documentation-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-documentation-version.html
	get-documentation-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-documentation-version.html
	get-documentation-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-documentation-versions.html
	update-documentation-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-documentation-version.html
    """

    write_parameter("apigateway", "create-documentation-version")