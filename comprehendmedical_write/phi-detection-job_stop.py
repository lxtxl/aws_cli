#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-phi-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-phi-detection-job.html
	list-phi-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-phi-detection-jobs.html
	start-phi-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-phi-detection-job.html
    """

    write_parameter("comprehendmedical", "stop-phi-detection-job")