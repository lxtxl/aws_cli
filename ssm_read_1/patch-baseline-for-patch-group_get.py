#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-patch-baseline-for-patch-group.html
if __name__ == '__main__':
    """
	deregister-patch-baseline-for-patch-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-patch-baseline-for-patch-group.html
	register-patch-baseline-for-patch-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-patch-baseline-for-patch-group.html
    """

    parameter_display_string = """
    # patch-group : The name of the patch group whose patch baseline should be retrieved.
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

    execute_one_parameter("ssm", "get-patch-baseline-for-patch-group", "patch-group", add_option_dict)