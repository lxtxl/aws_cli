#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/record-handler-progress.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # bearer-token : Reserved for use by the CloudFormation CLI .
    # operation-status : Reserved for use by the CloudFormation CLI .
Possible values:

PENDING
IN_PROGRESS
SUCCESS
FAILED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "record-handler-progress", "bearer-token", "operation-status", add_option_dict)
