#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-detector-version-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # detector-id : The detector ID.
    # detector-version-id : The detector version ID.
    # status : The new status.
Possible values:

DRAFT
ACTIVE
INACTIVE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("frauddetector", "update-detector-version-status", "detector-id", "detector-version-id", "status", add_option_dict)
