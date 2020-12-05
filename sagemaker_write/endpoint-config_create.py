#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-endpoint-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-endpoint-config.html
	describe-endpoint-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-endpoint-config.html
	list-endpoint-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-endpoint-configs.html
    """

    write_parameter("sagemaker", "create-endpoint-config")