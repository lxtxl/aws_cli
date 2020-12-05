#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/apply-archive-rule.html
if __name__ == '__main__':
    """
	create-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-archive-rule.html
	delete-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-archive-rule.html
	get-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-archive-rule.html
	list-archive-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-archive-rules.html
	update-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-archive-rule.html
    """

    parameter_display_string = """
    # analyzer-arn : The Amazon resource name (ARN) of the analyzer.
    # rule-name : The name of the rule to apply.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("accessanalyzer", "apply-archive-rule", "analyzer-arn", "rule-name", add_option_dict)
