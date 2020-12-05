#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-anomaly-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-anomaly-subscription.html
	get-anomaly-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-anomaly-subscriptions.html
	update-anomaly-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-anomaly-subscription.html
    """

    write_parameter("ce", "delete-anomaly-subscription")