#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-rule-priorities.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # rule-priorities : The rule priorities.
(structure)

Information about the priorities for the rules for a listener.
RuleArn -> (string)

The Amazon Resource Name (ARN) of the rule.

Priority -> (integer)

The rule priority.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elbv2", "set-rule-priorities", "rule-priorities", add_option_dict)





