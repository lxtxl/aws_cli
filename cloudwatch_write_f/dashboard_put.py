#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-dashboards.html
	get-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-dashboard.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-dashboards.html
    """

    write_parameter("cloudwatch", "put-dashboard")