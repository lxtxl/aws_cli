#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-theme.html
if __name__ == '__main__':
    """
	create-theme : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-theme.html
	delete-theme : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-theme.html
	describe-theme : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-theme.html
	list-themes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-themes.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the theme that youâre updating.
    # theme-id : The ID for the theme.
    # base-theme-id : The theme ID, defined by Amazon QuickSight, that a custom theme inherits from. All themes initially inherit from a default QuickSight theme.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "update-theme", "aws-account-id", "theme-id", "base-theme-id", add_option_dict)
