#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-model.html
	describe-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-model.html
	list-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-models.html
    """

    write_parameter("sagemaker", "create-model")