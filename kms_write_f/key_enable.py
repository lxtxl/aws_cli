#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html
	describe-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-key.html
	disable-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disable-key.html
	list-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-keys.html
    """

    write_parameter("kms", "enable-key")