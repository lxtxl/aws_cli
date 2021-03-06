#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-policy.html
	create-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy.html
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy.html
	get-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policies.html
    """

    write_parameter("iot", "detach-policy")