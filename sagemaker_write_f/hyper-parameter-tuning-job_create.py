#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-hyper-parameter-tuning-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-hyper-parameter-tuning-job.html
	list-hyper-parameter-tuning-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-hyper-parameter-tuning-jobs.html
	stop-hyper-parameter-tuning-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-hyper-parameter-tuning-job.html
    """

    write_parameter("sagemaker", "create-hyper-parameter-tuning-job")