#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-world-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-world-export-job.html
	describe-world-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-world-export-job.html
	list-world-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-world-export-jobs.html
    """

    write_parameter("robomaker", "create-world-export-job")