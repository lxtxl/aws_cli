#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-import-job.html
	list-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-import-jobs.html
    """

    write_parameter("sesv2", "create-import-job")