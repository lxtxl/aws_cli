#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-mitigation-action.html
if __name__ == '__main__':
    """
	delete-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-mitigation-action.html
	describe-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-mitigation-action.html
	list-mitigation-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-mitigation-actions.html
	update-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-mitigation-action.html
    """

    parameter_display_string = """
    # action-name : A friendly name for the action. Choose a friendly name that accurately describes the action (for example, EnableLoggingAction ).
    # role-arn : The ARN of the IAM role that is used to apply the mitigation action.
    # action-params : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot", "create-mitigation-action", "action-name", "role-arn", "action-params", add_option_dict)
