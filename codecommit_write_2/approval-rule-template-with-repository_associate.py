#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/associate-approval-rule-template-with-repository.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # approval-rule-template-name : The name for the approval rule template.
    # repository-name : The name of the repository that you want to associate with the template.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "associate-approval-rule-template-with-repository", "approval-rule-template-name", "repository-name", add_option_dict)
