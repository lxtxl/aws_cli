#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/describe-notification-rule.html
if __name__ == '__main__':
    """
	create-notification-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/create-notification-rule.html
	delete-notification-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/delete-notification-rule.html
	list-notification-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-notification-rules.html
	update-notification-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/update-notification-rule.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the notification rule.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("codestar-notifications", "describe-notification-rule", "arn", add_option_dict)