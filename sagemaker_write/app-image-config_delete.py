#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-app-image-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app-image-config.html
	describe-app-image-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-app-image-config.html
	list-app-image-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-app-image-configs.html
	update-app-image-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-app-image-config.html
    """

    write_parameter("sagemaker", "delete-app-image-config")