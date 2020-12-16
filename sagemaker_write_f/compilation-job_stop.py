#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-compilation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-compilation-job.html
	describe-compilation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-compilation-job.html
	list-compilation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-compilation-jobs.html
    """

    write_parameter("sagemaker", "stop-compilation-job")