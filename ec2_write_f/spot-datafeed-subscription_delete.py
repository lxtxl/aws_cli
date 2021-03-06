#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-spot-datafeed-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-spot-datafeed-subscription.html
	describe-spot-datafeed-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-datafeed-subscription.html
    """

    write_parameter("ec2", "delete-spot-datafeed-subscription")