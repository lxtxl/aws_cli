#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-description.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # approval-rule-template-name : The name of the template for which you want to update the description.
    # approval-rule-template-description : The updated description of the approval rule template.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "update-approval-rule-template-description", "approval-rule-template-name", "approval-rule-template-description", add_option_dict)
