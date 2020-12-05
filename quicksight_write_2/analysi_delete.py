#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-analysis.html
if __name__ == '__main__':
    """
	create-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-analysis.html
	describe-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-analysis.html
	restore-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/restore-analysis.html
	update-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-analysis.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account where you want to delete an analysis.
    # analysis-id : The ID of the analysis that youâre deleting.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "delete-analysis", "aws-account-id", "analysis-id", add_option_dict)
