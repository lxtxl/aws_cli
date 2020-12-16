#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-events-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-events-detection-job.html
	list-events-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-events-detection-jobs.html
	start-events-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-events-detection-job.html
    """

    write_parameter("comprehend", "stop-events-detection-job")