#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-action-target.html
if __name__ == '__main__':
    """
	delete-action-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-action-target.html
	describe-action-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-action-targets.html
	update-action-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-action-target.html
    """

    parameter_display_string = """
    # name : The name of the custom action target.
    # description : The description for the custom action target.
    # id : The ID for the custom action target.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("securityhub", "create-action-target", "name", "description", "id", add_option_dict)
