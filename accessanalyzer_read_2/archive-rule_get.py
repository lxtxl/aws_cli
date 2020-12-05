#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-archive-rule.html
if __name__ == '__main__':
    """
	apply-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/apply-archive-rule.html
	create-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-archive-rule.html
	delete-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-archive-rule.html
	list-archive-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-archive-rules.html
	update-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-archive-rule.html
    """

    parameter_display_string = """
    # analyzer-name : The name of the analyzer to retrieve rules from.
    # rule-name : The name of the rule to retrieve.
    """

    execute_two_parameter("accessanalyzer", "get-archive-rule", "analyzer-name", "rule-name", parameter_display_string)