#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-action-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-action-target.html
	describe-action-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-action-targets.html
	update-action-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-action-target.html
    """

    write_parameter("securityhub", "delete-action-target")