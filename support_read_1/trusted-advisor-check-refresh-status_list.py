#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-refresh-statuses.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # check-ids : The IDs of the Trusted Advisor checks to get the status of.

Note
If you specify the check ID of a check that is automatically refreshed, you might see an InvalidParameterValue error.

(string)
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("support", "describe-trusted-advisor-check-refresh-statuses", "check-ids", add_option_dict)