#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-forecast-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-forecast-export-job.html
	describe-forecast-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-forecast-export-job.html
	list-forecast-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-forecast-export-jobs.html
    """

    write_parameter("forecast", "delete-forecast-export-job")