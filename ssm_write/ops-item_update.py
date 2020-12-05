#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-ops-item.html
	describe-ops-items : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-ops-items.html
	get-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-item.html
    """

    write_parameter("ssm", "update-ops-item")