#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/create-lifecycle-policy.html
	delete-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/delete-lifecycle-policy.html
	get-lifecycle-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/get-lifecycle-policies.html
	get-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/get-lifecycle-policy.html
    """

    write_parameter("dlm", "update-lifecycle-policy")