#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/remove-targets.html
if __name__ == '__main__':
    """
	put-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-targets.html
    """

    parameter_display_string = """
    # rule : The name of the rule.
    # ids : The IDs of the targets to remove from the rule.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("events", "remove-targets", "rule", "ids", add_option_dict)
