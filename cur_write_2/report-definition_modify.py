#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/modify-report-definition.html
if __name__ == '__main__':
    """
	delete-report-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/delete-report-definition.html
	describe-report-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/describe-report-definitions.html
	put-report-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/put-report-definition.html
    """

    parameter_display_string = """
    # report-name : The name of the report that you want to create. The name must be unique, is case sensitive, and canât include spaces.
    # report-definition : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cur", "modify-report-definition", "report-name", "report-definition", add_option_dict)
