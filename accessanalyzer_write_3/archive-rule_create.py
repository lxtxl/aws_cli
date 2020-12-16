#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-archive-rule.html
if __name__ == '__main__':
    """
	apply-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/apply-archive-rule.html
	delete-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-archive-rule.html
	get-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-archive-rule.html
	list-archive-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-archive-rules.html
	update-archive-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-archive-rule.html
    """

    parameter_display_string = """
    # analyzer-name : The name of the created analyzer.
    # filter : The criteria for the rule.
key -> (string)
value -> (structure)

The criteria to use in the filter that defines the archive rule.
contains -> (list)

A âcontainsâ operator to match for the filter used to create the rule.
(string)

eq -> (list)

An âequalsâ operator to match for the filter used to create the rule.
(string)

exists -> (boolean)

An âexistsâ operator to match for the filter used to create the rule.

neq -> (list)

A ânot equalsâ operator to match for the filter used to create the rule.
(string)
    # rule-name : The name of the rule to create.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("accessanalyzer", "create-archive-rule", "analyzer-name", "filter", "rule-name", add_option_dict)
