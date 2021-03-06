#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-domain-name.html
	get-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-name.html
	get-domain-names : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-names.html
	update-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-domain-name.html
    """

    write_parameter("apigateway", "create-domain-name")