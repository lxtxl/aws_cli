#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-state.html
if __name__ == '__main__':
    """
	get-pull-request-approval-states : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request-approval-states.html
    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID of the pull request.
    # revision-id : The system-generated ID of the revision.
    # approval-state : The approval state to associate with the user on the pull request.
Possible values:

APPROVE
REVOKE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codecommit", "update-pull-request-approval-state", "pull-request-id", "revision-id", "approval-state", add_option_dict)
