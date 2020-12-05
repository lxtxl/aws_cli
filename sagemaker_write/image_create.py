#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-image.html
	describe-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-image.html
	list-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-images.html
	update-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-image.html
    """

    write_parameter("sagemaker", "create-image")