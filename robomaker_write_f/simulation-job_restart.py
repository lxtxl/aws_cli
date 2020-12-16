#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-simulation-job.html
	create-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-simulation-job.html
	describe-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-job.html
	list-simulation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-jobs.html
    """

    write_parameter("robomaker", "restart-simulation-job")