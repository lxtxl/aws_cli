#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workteam.html
	delete-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-workteam.html
	describe-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-workteam.html
	list-workteams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workteams.html
    """

    write_parameter("sagemaker", "update-workteam")