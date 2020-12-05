#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-segment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-segment.html
	get-segment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-segment.html
	get-segments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-segments.html
	update-segment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-segment.html
    """

    write_parameter("pinpoint", "delete-segment")