#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-targets.html
if __name__ == '__main__':
    """
	create-assessment-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-assessment-target.html
	delete-assessment-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-target.html
	list-assessment-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-targets.html
	update-assessment-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/update-assessment-target.html
    """

    parameter_display_string = """
    # assessment-target-arns : The ARNs that specifies the assessment targets that you want to describe.
(string)
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

    execute_one_parameter("inspector", "describe-assessment-targets", "assessment-target-arns", add_option_dict)