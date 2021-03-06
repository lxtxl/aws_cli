#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-lag : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-lag.html
	describe-lags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-lags.html
	update-lag : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-lag.html
    """

    write_parameter("directconnect", "delete-lag")