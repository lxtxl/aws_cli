#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-job-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-job-runs.html
	stop-job-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/stop-job-run.html
    """

    write_parameter("databrew", "start-job-run")