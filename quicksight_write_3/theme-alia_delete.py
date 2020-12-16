#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-theme-alias.html
if __name__ == '__main__':
    """
	create-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-theme-alias.html
	describe-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-theme-alias.html
	update-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-theme-alias.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the theme alias to delete.
    # theme-id : The ID for the theme that the specified alias is for.
    # alias-name : The unique name for the theme alias to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "delete-theme-alias", "aws-account-id", "theme-id", "alias-name", add_option_dict)
