#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/get-report-group-trend.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # report-group-arn : 
    # trend-field : Possible values:

PASS_RATE
DURATION
TOTAL
LINE_COVERAGE
LINES_COVERED
LINES_MISSED
BRANCH_COVERAGE
BRANCHES_COVERED
BRANCHES_MISSED
    """

    execute_two_parameter("codebuild", "get-report-group-trend", "report-group-arn", "trend-field", parameter_display_string)