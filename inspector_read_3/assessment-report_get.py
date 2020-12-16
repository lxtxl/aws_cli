#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/get-assessment-report.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # assessment-run-arn : The ARN that specifies the assessment run for which you want to generate a report.
    # report-file-format : Specifies the file format (html or pdf) of the assessment report that you want to generate.
Possible values:

HTML
PDF
    """

    execute_two_parameter("inspector", "get-assessment-report", "assessment-run-arn", "report-file-format", parameter_display_string)