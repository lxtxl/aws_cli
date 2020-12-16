#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-processing-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-processing-job.html
	describe-processing-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-processing-job.html
	list-processing-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-processing-jobs.html
    """

    write_parameter("sagemaker", "stop-processing-job")