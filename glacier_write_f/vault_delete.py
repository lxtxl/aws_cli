#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-vault : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/create-vault.html
	describe-vault : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/describe-vault.html
	list-vaults : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-vaults.html
    """

    write_parameter("glacier", "delete-vault")