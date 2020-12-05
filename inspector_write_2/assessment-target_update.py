#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/update-assessment-target.html
if __name__ == '__main__':
    """
	create-assessment-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-assessment-target.html
	delete-assessment-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-target.html
	describe-assessment-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-targets.html
	list-assessment-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-targets.html
    """

    parameter_display_string = """
    # assessment-target-arn : The ARN of the assessment target that you want to update.
    # assessment-target-name : The name of the assessment target that you want to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("inspector", "update-assessment-target", "assessment-target-arn", "assessment-target-name", add_option_dict)
