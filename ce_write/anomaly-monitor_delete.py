#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-anomaly-monitor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-anomaly-monitor.html
	get-anomaly-monitors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-anomaly-monitors.html
	update-anomaly-monitor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-anomaly-monitor.html
    """

    write_parameter("ce", "delete-anomaly-monitor")