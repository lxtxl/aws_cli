#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-default-patch-baseline.html
if __name__ == '__main__':
    """
	get-default-patch-baseline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-default-patch-baseline.html
    """

    parameter_display_string = """
    # baseline-id : The ID of the patch baseline that should be the default patch baseline.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "register-default-patch-baseline", "baseline-id", add_option_dict)





