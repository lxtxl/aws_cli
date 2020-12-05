#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-pull-request-approval-rule.html
if __name__ == '__main__':
    """
	create-pull-request-approval-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request-approval-rule.html
	evaluate-pull-request-approval-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/evaluate-pull-request-approval-rules.html
	override-pull-request-approval-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/override-pull-request-approval-rules.html
    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID of the pull request that contains the approval rule you want to delete.
    # approval-rule-name : The name of the approval rule you want to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "delete-pull-request-approval-rule", "pull-request-id", "approval-rule-name", add_option_dict)
