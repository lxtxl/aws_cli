#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-notebook-instance.html
	describe-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-notebook-instance.html
	list-notebook-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-notebook-instances.html
	start-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/start-notebook-instance.html
	stop-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-notebook-instance.html
	update-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-notebook-instance.html
    """

    write_parameter("sagemaker", "create-notebook-instance")