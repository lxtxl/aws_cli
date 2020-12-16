#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-feature-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-feature-group.html
	describe-feature-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-feature-group.html
	list-feature-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-feature-groups.html
    """

    write_parameter("sagemaker", "delete-feature-group")