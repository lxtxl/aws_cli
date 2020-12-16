#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-jobs.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html
	submit-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html
	terminate-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/terminate-job.html
    """

    write_parameter("batch", "cancel-job")