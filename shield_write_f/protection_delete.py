#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-protection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html
	describe-protection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-protection.html
	list-protections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protections.html
    """

    write_parameter("shield", "delete-protection")