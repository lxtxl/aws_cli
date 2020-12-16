#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-notebook-instance-lifecycle-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-notebook-instance-lifecycle-config.html
	describe-notebook-instance-lifecycle-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-notebook-instance-lifecycle-config.html
	list-notebook-instance-lifecycle-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-notebook-instance-lifecycle-configs.html
	update-notebook-instance-lifecycle-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-notebook-instance-lifecycle-config.html
    """

    write_parameter("sagemaker", "delete-notebook-instance-lifecycle-config")