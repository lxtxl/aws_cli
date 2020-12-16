#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-flow.html
	delete-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/delete-flow.html
	describe-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow.html
	list-flows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/list-flows.html
	start-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/start-flow.html
	stop-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/stop-flow.html
    """

    write_parameter("mediaconnect", "update-flow")