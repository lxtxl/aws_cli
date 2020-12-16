#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-projects.html
    """

    write_parameter("sagemaker", "create-project")