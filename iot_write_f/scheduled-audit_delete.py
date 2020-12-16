#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-scheduled-audit.html
	describe-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-scheduled-audit.html
	list-scheduled-audits : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-scheduled-audits.html
	update-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-scheduled-audit.html
    """

    write_parameter("iot", "delete-scheduled-audit")