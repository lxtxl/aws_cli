#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-client-certificate.html
	get-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-client-certificate.html
	get-client-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-client-certificates.html
	update-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-client-certificate.html
    """

    write_parameter("apigateway", "generate-client-certificate")