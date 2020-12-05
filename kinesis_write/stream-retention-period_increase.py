#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	decrease-stream-retention-period : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/decrease-stream-retention-period.html
    """

    write_parameter("kinesis", "increase-stream-retention-period")