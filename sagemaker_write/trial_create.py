#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-trial.html
	describe-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-trial.html
	list-trials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-trials.html
	update-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-trial.html
    """

    write_parameter("sagemaker", "create-trial")