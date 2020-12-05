#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-runs.html
if __name__ == '__main__':
    """
	delete-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-run.html
	list-assessment-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-runs.html
	start-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/start-assessment-run.html
	stop-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/stop-assessment-run.html
    """

    parameter_display_string = """
    # assessment-run-arns : The ARN that specifies the assessment run that you want to describe.
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

    execute_one_parameter("inspector", "describe-assessment-runs", "assessment-run-arns", add_option_dict)