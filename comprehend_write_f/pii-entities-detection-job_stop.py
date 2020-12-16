#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-pii-entities-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-pii-entities-detection-job.html
	list-pii-entities-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-pii-entities-detection-jobs.html
	start-pii-entities-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-pii-entities-detection-job.html
    """

    write_parameter("comprehend", "stop-pii-entities-detection-job")