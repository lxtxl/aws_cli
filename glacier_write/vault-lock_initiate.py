#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	abort-vault-lock : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/abort-vault-lock.html
	complete-vault-lock : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/complete-vault-lock.html
	get-vault-lock : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-lock.html
    """

    write_parameter("glacier", "initiate-vault-lock")