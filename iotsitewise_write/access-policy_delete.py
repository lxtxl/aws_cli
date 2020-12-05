#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-access-policy.html
	describe-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-access-policy.html
	list-access-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-access-policies.html
	update-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-access-policy.html
    """

    write_parameter("iotsitewise", "delete-access-policy")