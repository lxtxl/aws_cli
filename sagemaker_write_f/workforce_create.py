#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-workforce.html
	describe-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-workforce.html
	list-workforces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workforces.html
	update-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-workforce.html
    """

    write_parameter("sagemaker", "create-workforce")