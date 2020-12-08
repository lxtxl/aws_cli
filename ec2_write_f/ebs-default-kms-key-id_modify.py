#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-ebs-default-kms-key-id : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ebs-default-kms-key-id.html
	reset-ebs-default-kms-key-id : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-ebs-default-kms-key-id.html
    """

    write_parameter("ec2", "modify-ebs-default-kms-key-id")