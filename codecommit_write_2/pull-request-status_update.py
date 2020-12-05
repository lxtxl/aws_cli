#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
    # pull-request-status : The status of the pull request. The only valid operations are to update the status from OPEN to OPEN , OPEN to CLOSED or from CLOSED to CLOSED .
Possible values:

OPEN
CLOSED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "update-pull-request-status", "pull-request-id", "pull-request-status", add_option_dict)
