#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-business-report-schedule.html
	list-business-report-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-business-report-schedules.html
	update-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-business-report-schedule.html
    """

    write_parameter("alexaforbusiness", "create-business-report-schedule")