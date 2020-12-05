#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-labeling-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-labeling-job.html
	describe-labeling-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-labeling-job.html
	list-labeling-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-labeling-jobs.html
    """

    write_parameter("sagemaker", "stop-labeling-job")