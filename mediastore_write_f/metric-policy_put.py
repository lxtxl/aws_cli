#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-metric-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-metric-policy.html
	get-metric-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-metric-policy.html
    """

    write_parameter("mediastore", "put-metric-policy")