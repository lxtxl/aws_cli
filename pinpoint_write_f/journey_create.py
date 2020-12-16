#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-journey.html
	get-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-journey.html
	list-journeys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/list-journeys.html
	update-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-journey.html
    """

    write_parameter("pinpoint", "create-journey")