#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-audit-suppression.html
if __name__ == '__main__':
    """
	create-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-audit-suppression.html
	delete-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-audit-suppression.html
	describe-audit-suppression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-suppression.html
	list-audit-suppressions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-suppressions.html
    """

    parameter_display_string = """
    # check-name : An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)
    # resource-identifier : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "update-audit-suppression", "check-name", "resource-identifier", add_option_dict)
