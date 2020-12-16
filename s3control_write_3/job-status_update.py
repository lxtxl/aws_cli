#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/update-job-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The account ID of the requester.
    # job-id : The ID of the job whose status you want to update.
    # requested-job-status : The status that you want to move the specified job to.
Possible values:

Cancelled
Ready
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3control", "update-job-status", "account-id", "job-id", "requested-job-status", add_option_dict)
