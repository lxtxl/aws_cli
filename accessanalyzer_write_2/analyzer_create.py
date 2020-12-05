#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-analyzer.html
if __name__ == '__main__':
    """
	delete-analyzer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-analyzer.html
	get-analyzer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-analyzer.html
	list-analyzers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-analyzers.html
    """

    parameter_display_string = """
    # analyzer-name : The name of the analyzer to create.
    # type : The type of analyzer to create. Only ACCOUNT analyzers are supported. You can create only one analyzer per account per Region.
Possible values:

ACCOUNT
ORGANIZATION
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("accessanalyzer", "create-analyzer", "analyzer-name", "type", add_option_dict)
