#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-image-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-image-version.html
	describe-image-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-image-version.html
	list-image-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-image-versions.html
    """

    write_parameter("sagemaker", "delete-image-version")