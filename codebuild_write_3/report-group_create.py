#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/create-report-group.html
if __name__ == '__main__':
    """
	delete-report-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-report-group.html
	list-report-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-report-groups.html
	update-report-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-report-group.html
    """

    parameter_display_string = """
    # name : The name of the report group.
    # type : The type of report group.
Possible values:

TEST
CODE_COVERAGE
    # export-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codebuild", "create-report-group", "name", "type", "export-config", add_option_dict)
