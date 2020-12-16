#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-theme-alias.html
if __name__ == '__main__':
    """
	create-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-theme-alias.html
	delete-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-theme-alias.html
	update-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-theme-alias.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the theme alias that youâre describing.
    # theme-id : The ID for the theme.
    """

    execute_two_parameter("quicksight", "describe-theme-alias", "aws-account-id", "theme-id", parameter_display_string)