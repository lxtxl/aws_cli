#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint.html
	describe-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-endpoint.html
	list-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-endpoints.html
	update-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-endpoint.html
    """

    write_parameter("sagemaker", "delete-endpoint")