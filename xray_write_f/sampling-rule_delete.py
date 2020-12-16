#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-sampling-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/create-sampling-rule.html
	get-sampling-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-sampling-rules.html
	update-sampling-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/update-sampling-rule.html
    """

    write_parameter("xray", "delete-sampling-rule")