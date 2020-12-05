#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-content.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # approval-rule-template-name : The name of the approval rule template where you want to update the content of the rule.
    # new-rule-content : The content that replaces the existing content of the rule. Content statements must be complete. You cannot provide only the changes.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "update-approval-rule-template-content", "approval-rule-template-name", "new-rule-content", add_option_dict)
