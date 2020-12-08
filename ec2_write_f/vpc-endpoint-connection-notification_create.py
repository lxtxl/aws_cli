#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-vpc-endpoint-connection-notifications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoint-connection-notifications.html
	describe-vpc-endpoint-connection-notifications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-connection-notifications.html
	modify-vpc-endpoint-connection-notification : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint-connection-notification.html
    """

    write_parameter("ec2", "create-vpc-endpoint-connection-notification")