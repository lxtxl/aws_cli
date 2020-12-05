#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-target.html
if __name__ == '__main__':
    """
	create-assessment-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-assessment-target.html
	describe-assessment-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-targets.html
	list-assessment-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-targets.html
	update-assessment-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/update-assessment-target.html
    """

    parameter_display_string = """
    # assessment-target-arn : The ARN that specifies the assessment target that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("inspector", "delete-assessment-target", "assessment-target-arn", add_option_dict)





