#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-audit-suppression.html
	describe-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-suppression.html
	list-audit-suppressions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-suppressions.html
	update-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-audit-suppression.html
    """

    write_parameter("iot", "delete-audit-suppression")