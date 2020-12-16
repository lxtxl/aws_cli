#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-listener.html
	describe-listeners : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listeners.html
	modify-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-listener.html
    """

    write_parameter("elbv2", "create-listener")