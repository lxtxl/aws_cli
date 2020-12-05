#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-trust : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-trust.html
	delete-trust : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-trust.html
	describe-trusts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-trusts.html
	verify-trust : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/verify-trust.html
    """

    write_parameter("ds", "update-trust")