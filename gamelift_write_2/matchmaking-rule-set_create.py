#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-matchmaking-rule-set.html
if __name__ == '__main__':
    """
	delete-matchmaking-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-matchmaking-rule-set.html
	describe-matchmaking-rule-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking-rule-sets.html
	validate-matchmaking-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/validate-matchmaking-rule-set.html
    """

    parameter_display_string = """
    # name : A unique identifier for a matchmaking rule set. A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional name field in the rule set body.
    # rule-set-body : A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "create-matchmaking-rule-set", "name", "rule-set-body", add_option_dict)
