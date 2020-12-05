#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/approve-assignment.html
if __name__ == '__main__':
    """
	get-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-assignment.html
	reject-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/reject-assignment.html
    """

    parameter_display_string = """
    # assignment-id : The ID of the assignment. The assignment must correspond to a HIT created by the Requester.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mturk", "approve-assignment", "assignment-id", add_option_dict)





