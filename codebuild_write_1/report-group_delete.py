#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-report-group.html
if __name__ == '__main__':
    """
	create-report-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/create-report-group.html
	list-report-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-report-groups.html
	update-report-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-report-group.html
    """

    parameter_display_string = """
    # arn : The ARN of the report group to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codebuild", "delete-report-group", "arn", add_option_dict)





