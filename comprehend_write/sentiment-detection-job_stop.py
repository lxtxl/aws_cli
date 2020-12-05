#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-sentiment-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-sentiment-detection-job.html
	list-sentiment-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-sentiment-detection-jobs.html
	start-sentiment-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-sentiment-detection-job.html
    """

    write_parameter("comprehend", "stop-sentiment-detection-job")