#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-template.html
if __name__ == '__main__':
    """
	create-assessment-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-assessment-template.html
	describe-assessment-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-templates.html
	list-assessment-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-templates.html
    """

    parameter_display_string = """
    # assessment-template-arn : The ARN that specifies the assessment template that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("inspector", "delete-assessment-template", "assessment-template-arn", add_option_dict)





