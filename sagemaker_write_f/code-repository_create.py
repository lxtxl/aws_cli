#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-code-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-code-repository.html
	describe-code-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-code-repository.html
	list-code-repositories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-code-repositories.html
	update-code-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-code-repository.html
    """

    write_parameter("sagemaker", "create-code-repository")