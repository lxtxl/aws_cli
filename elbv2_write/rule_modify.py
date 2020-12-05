#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-rule.html
	delete-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-rule.html
	describe-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-rules.html
    """

    write_parameter("elbv2", "modify-rule")