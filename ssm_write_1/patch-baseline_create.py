#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-patch-baseline.html
if __name__ == '__main__':
    """
	delete-patch-baseline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-patch-baseline.html
	describe-patch-baselines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-baselines.html
	get-patch-baseline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-patch-baseline.html
	update-patch-baseline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-patch-baseline.html
    """

    parameter_display_string = """
    # name : The name of the patch baseline.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "create-patch-baseline", "name", add_option_dict)





