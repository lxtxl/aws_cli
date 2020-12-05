#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-analysis.html
if __name__ == '__main__':
    """
	create-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-analysis.html
	delete-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-analysis.html
	restore-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/restore-analysis.html
	update-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-analysis.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the analysis. You must be using the AWS account that the analysis is in.
    # analysis-id : The ID of the analysis that youâre describing. The ID is part of the URL of the analysis.
    """

    execute_two_parameter("quicksight", "describe-analysis", "aws-account-id", "analysis-id", parameter_display_string)