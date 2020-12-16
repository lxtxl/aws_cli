#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-flow-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-flow-definition.html
	describe-flow-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-flow-definition.html
	list-flow-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-flow-definitions.html
    """

    write_parameter("sagemaker", "delete-flow-definition")