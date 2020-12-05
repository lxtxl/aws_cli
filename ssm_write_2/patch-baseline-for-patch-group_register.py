#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-patch-baseline-for-patch-group.html
if __name__ == '__main__':
    """
	deregister-patch-baseline-for-patch-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-patch-baseline-for-patch-group.html
	get-patch-baseline-for-patch-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-patch-baseline-for-patch-group.html
    """

    parameter_display_string = """
    # baseline-id : The ID of the patch baseline to register the patch group with.
    # patch-group : The name of the patch group that should be registered with the patch baseline.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "register-patch-baseline-for-patch-group", "baseline-id", "patch-group", add_option_dict)
