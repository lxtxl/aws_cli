#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-delivery-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channels.html
	put-delivery-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-delivery-channel.html
    """

    write_parameter("configservice", "delete-delivery-channel")