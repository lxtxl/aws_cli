#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-rx-norm-inference-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-rx-norm-inference-job.html
	list-rx-norm-inference-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-rx-norm-inference-jobs.html
	start-rx-norm-inference-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-rx-norm-inference-job.html
    """

    write_parameter("comprehendmedical", "stop-rx-norm-inference-job")