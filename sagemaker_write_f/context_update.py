#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-context.html
	delete-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-context.html
	describe-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-context.html
	list-contexts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-contexts.html
    """

    write_parameter("sagemaker", "update-context")