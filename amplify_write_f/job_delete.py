#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-jobs.html
	start-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/start-job.html
	stop-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/stop-job.html
    """

    write_parameter("amplify", "delete-job")