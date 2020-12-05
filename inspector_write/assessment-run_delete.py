#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-assessment-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-runs.html
	list-assessment-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-runs.html
	start-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/start-assessment-run.html
	stop-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/stop-assessment-run.html
    """

    write_parameter("inspector", "delete-assessment-run")