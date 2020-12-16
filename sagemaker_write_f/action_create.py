#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-action.html
	describe-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-action.html
	list-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-actions.html
	update-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-action.html
    """

    write_parameter("sagemaker", "create-action")