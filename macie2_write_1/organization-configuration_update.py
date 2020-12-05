#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-organization-configuration.html
if __name__ == '__main__':
    """
	describe-organization-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/describe-organization-configuration.html
    """

    parameter_display_string = """
    # auto-enable | --no-auto-enable : Specifies whether Amazon Macie is enabled automatically for each account, when the account is added to the AWS organization.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("macie2", "update-organization-configuration", "auto-enable | --no-auto-enable", add_option_dict)





