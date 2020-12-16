#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-artifact.html
	describe-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-artifact.html
	list-artifacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-artifacts.html
	update-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-artifact.html
    """

    write_parameter("sagemaker", "delete-artifact")