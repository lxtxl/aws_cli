#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-dominant-language-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-dominant-language-detection-job.html
	list-dominant-language-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-dominant-language-detection-jobs.html
	stop-dominant-language-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-dominant-language-detection-job.html
    """

    write_parameter("comprehend", "start-dominant-language-detection-job")