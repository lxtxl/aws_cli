#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/start-assessment-run.html
if __name__ == '__main__':
    """
	delete-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-run.html
	describe-assessment-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-runs.html
	list-assessment-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-runs.html
	stop-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/stop-assessment-run.html
    """

    parameter_display_string = """
    # assessment-template-arn : The ARN of the assessment template of the assessment run that you want to start.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("inspector", "start-assessment-run", "assessment-template-arn", add_option_dict)





