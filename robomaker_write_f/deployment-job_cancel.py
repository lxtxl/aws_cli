#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-deployment-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-deployment-job.html
	describe-deployment-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-deployment-job.html
	list-deployment-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-deployment-jobs.html
	sync-deployment-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/sync-deployment-job.html
    """

    write_parameter("robomaker", "cancel-deployment-job")