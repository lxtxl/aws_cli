#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding.html
if __name__ == '__main__':
    """
	list-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-findings.html
	update-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-findings.html
    """

    parameter_display_string = """
    # analyzer-arn : The ARN of the analyzer that generated the finding.
    # id : The ID of the finding to retrieve.
    """

    execute_two_parameter("accessanalyzer", "get-finding", "analyzer-arn", "id", parameter_display_string)