#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-suppression.html
if __name__ == '__main__':
    """
	create-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-audit-suppression.html
	delete-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-audit-suppression.html
	list-audit-suppressions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-suppressions.html
	update-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-audit-suppression.html
    """

    parameter_display_string = """
    # check-name : An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)
    # resource-identifier : 
    """

    execute_two_parameter("iot", "describe-audit-suppression", "check-name", "resource-identifier", parameter_display_string)