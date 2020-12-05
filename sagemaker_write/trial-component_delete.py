#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/associate-trial-component.html
	create-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-trial-component.html
	describe-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-trial-component.html
	disassociate-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/disassociate-trial-component.html
	list-trial-components : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-trial-components.html
	update-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-trial-component.html
    """

    write_parameter("sagemaker", "delete-trial-component")