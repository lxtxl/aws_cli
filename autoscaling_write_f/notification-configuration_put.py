#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-notification-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-notification-configuration.html
	describe-notification-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-notification-configurations.html
    """

    write_parameter("autoscaling", "put-notification-configuration")