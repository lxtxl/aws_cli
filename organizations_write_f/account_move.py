#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-account.html
	describe-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-account.html
	list-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-accounts.html
    """

    write_parameter("organizations", "move-account")