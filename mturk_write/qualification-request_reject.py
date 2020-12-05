#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	accept-qualification-request : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/accept-qualification-request.html
	list-qualification-requests : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-qualification-requests.html
    """

    write_parameter("mturk", "reject-qualification-request")