#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-admin-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/associate-admin-account.html
	get-admin-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-admin-account.html
    """

    write_parameter("fms", "disassociate-admin-account")