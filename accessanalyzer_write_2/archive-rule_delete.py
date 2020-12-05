#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-archive-rule.html
if __name__ == '__main__':
    """
	apply-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/apply-archive-rule.html
	create-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-archive-rule.html
	get-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-archive-rule.html
	list-archive-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-archive-rules.html
	update-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-archive-rule.html
    """

    parameter_display_string = """
    # analyzer-name : The name of the analyzer that associated with the archive rule to delete.
    # rule-name : The name of the rule to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("accessanalyzer", "delete-archive-rule", "analyzer-name", "rule-name", add_option_dict)
