#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-traffic-mirror-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-traffic-mirror-filter.html
	describe-traffic-mirror-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-traffic-mirror-filters.html
    """

    write_parameter("ec2", "create-traffic-mirror-filter")