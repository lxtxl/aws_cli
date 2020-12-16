#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-scheduled-audit.html
if __name__ == '__main__':
    """
	delete-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-scheduled-audit.html
	describe-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-scheduled-audit.html
	list-scheduled-audits : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-scheduled-audits.html
	update-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-scheduled-audit.html
    """

    parameter_display_string = """
    # frequency : How often the scheduled audit takes place. Can be one of âDAILYâ, âWEEKLYâ, âBIWEEKLYâ or âMONTHLYâ. The start time of each audit is determined by the system.
Possible values:

DAILY
WEEKLY
BIWEEKLY
MONTHLY
    # target-check-names : Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)
(string)

An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)
    # scheduled-audit-name : The name you want to give to the scheduled audit. (Max. 128 chars)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot", "create-scheduled-audit", "frequency", "target-check-names", "scheduled-audit-name", add_option_dict)
