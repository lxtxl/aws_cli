#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-schedule.html
	describe-snapshot-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-schedules.html
	modify-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-schedule.html
    """

    write_parameter("redshift", "delete-snapshot-schedule")