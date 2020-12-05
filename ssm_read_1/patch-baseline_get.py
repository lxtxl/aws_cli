#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-patch-baseline.html
if __name__ == '__main__':
    """
	create-patch-baseline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-patch-baseline.html
	delete-patch-baseline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-patch-baseline.html
	describe-patch-baselines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-baselines.html
	update-patch-baseline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-patch-baseline.html
    """

    parameter_display_string = """
    # baseline-id : The ID of the patch baseline to retrieve.
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

    execute_one_parameter("ssm", "get-patch-baseline", "baseline-id", add_option_dict)