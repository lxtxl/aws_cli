#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/reject-assignment.html
if __name__ == '__main__':
    """
	approve-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/approve-assignment.html
	get-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-assignment.html
    """

    parameter_display_string = """
    # assignment-id : The ID of the assignment. The assignment must correspond to a HIT created by the Requester.
    # requester-feedback : A message for the Worker, which the Worker can see in the Status section of the web site.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mturk", "reject-assignment", "assignment-id", "requester-feedback", add_option_dict)
