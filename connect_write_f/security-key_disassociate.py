#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-security-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-security-key.html
	list-security-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-security-keys.html
    """

    write_parameter("connect", "disassociate-security-key")