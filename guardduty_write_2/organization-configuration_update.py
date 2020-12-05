#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-organization-configuration.html
if __name__ == '__main__':
    """
	describe-organization-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/describe-organization-configuration.html
    """

    parameter_display_string = """
    # detector-id : The ID of the detector to update the delegated administrator for.
    # auto-enable | --no-auto-enable : Indicates whether to automatically enable member accounts in the organization.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "update-organization-configuration", "detector-id", "auto-enable | --no-auto-enable", add_option_dict)
