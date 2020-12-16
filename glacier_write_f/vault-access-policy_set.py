#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-vault-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-vault-access-policy.html
	get-vault-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-access-policy.html
    """

    write_parameter("glacier", "set-vault-access-policy")