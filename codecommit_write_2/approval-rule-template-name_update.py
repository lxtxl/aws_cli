#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-name.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # old-approval-rule-template-name : The current name of the approval rule template.
    # new-approval-rule-template-name : The new name you want to apply to the approval rule template.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "update-approval-rule-template-name", "old-approval-rule-template-name", "new-approval-rule-template-name", add_option_dict)
