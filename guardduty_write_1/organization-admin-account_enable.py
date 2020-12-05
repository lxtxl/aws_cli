#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/enable-organization-admin-account.html
if __name__ == '__main__':
    """
	disable-organization-admin-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disable-organization-admin-account.html
	list-organization-admin-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-organization-admin-accounts.html
    """

    parameter_display_string = """
    # admin-account-id : The AWS Account ID for the organization account to be enabled as a GuardDuty delegated administrator.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("guardduty", "enable-organization-admin-account", "admin-account-id", add_option_dict)





