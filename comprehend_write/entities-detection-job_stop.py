#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-entities-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-entities-detection-job.html
	list-entities-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-entities-detection-jobs.html
	start-entities-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-entities-detection-job.html
    """

    write_parameter("comprehend", "stop-entities-detection-job")