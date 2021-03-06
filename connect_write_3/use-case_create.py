#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-use-case.html
if __name__ == '__main__':
    """
	delete-use-case : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/delete-use-case.html
	list-use-cases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-use-cases.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # integration-association-id : The identifier for the AppIntegration association.
    # use-case-type : The type of use case to associate to the AppIntegration association. Each AppIntegration association can have only one of each use case type.
Possible values:

RULES_EVALUATION
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "create-use-case", "instance-id", "integration-association-id", "use-case-type", add_option_dict)
