#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-monitoring-schedule.html
	delete-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-monitoring-schedule.html
	describe-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-monitoring-schedule.html
	list-monitoring-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-monitoring-schedules.html
	stop-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-monitoring-schedule.html
	update-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-monitoring-schedule.html
    """

    write_parameter("sagemaker", "start-monitoring-schedule")