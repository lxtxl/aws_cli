#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-canary.html
	delete-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html
	describe-canaries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-canaries.html
	get-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary.html
	start-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary.html
	stop-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/stop-canary.html
    """

    write_parameter("synthetics", "update-canary")