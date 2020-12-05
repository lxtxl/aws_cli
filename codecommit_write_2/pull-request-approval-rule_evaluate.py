#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/evaluate-pull-request-approval-rules.html
if __name__ == '__main__':
    """
	create-pull-request-approval-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request-approval-rule.html
	delete-pull-request-approval-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-pull-request-approval-rule.html
	override-pull-request-approval-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/override-pull-request-approval-rules.html
    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID of the pull request you want to evaluate.
    # revision-id : The system-generated ID for the pull request revision. To retrieve the most recent revision ID for a pull request, use  GetPullRequest .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "evaluate-pull-request-approval-rules", "pull-request-id", "revision-id", add_option_dict)
