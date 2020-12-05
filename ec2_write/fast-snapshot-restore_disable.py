#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-fast-snapshot-restores : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fast-snapshot-restores.html
	enable-fast-snapshot-restores : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-snapshot-restores.html
    """

    write_parameter("ec2", "disable-fast-snapshot-restores")