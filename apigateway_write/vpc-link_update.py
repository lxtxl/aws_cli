#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-vpc-link.html
	delete-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-vpc-link.html
	get-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-vpc-link.html
	get-vpc-links : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-vpc-links.html
    """

    write_parameter("apigateway", "update-vpc-link")