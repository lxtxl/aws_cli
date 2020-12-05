#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/accept-qualification-request.html
if __name__ == '__main__':
    """
	list-qualification-requests : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-qualification-requests.html
	reject-qualification-request : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/reject-qualification-request.html
    """

    parameter_display_string = """
    # qualification-request-id : The ID of the Qualification request, as returned by the GetQualificationRequests operation.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mturk", "accept-qualification-request", "qualification-request-id", add_option_dict)





