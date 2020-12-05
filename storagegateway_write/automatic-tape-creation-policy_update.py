#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-automatic-tape-creation-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-automatic-tape-creation-policy.html
	list-automatic-tape-creation-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-automatic-tape-creation-policies.html
    """

    write_parameter("storagegateway", "update-automatic-tape-creation-policy")