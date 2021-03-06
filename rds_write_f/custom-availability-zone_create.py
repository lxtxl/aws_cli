#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-custom-availability-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-custom-availability-zone.html
	describe-custom-availability-zones : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-custom-availability-zones.html
    """

    write_parameter("rds", "create-custom-availability-zone")