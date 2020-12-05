#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-auto-ml-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-auto-ml-job.html
	describe-auto-ml-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-auto-ml-job.html
	list-auto-ml-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-auto-ml-jobs.html
    """

    write_parameter("sagemaker", "stop-auto-ml-job")