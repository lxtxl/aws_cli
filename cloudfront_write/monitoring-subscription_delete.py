#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-monitoring-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-monitoring-subscription.html
	get-monitoring-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-monitoring-subscription.html
    """

    write_parameter("cloudfront", "delete-monitoring-subscription")