#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-policy.html
if __name__ == '__main__':
    """
	describe-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-policies.html
	execute-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/execute-policy.html
    """

    parameter_display_string = """
    # policy-name : The name or Amazon Resource Name (ARN) of the policy.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("autoscaling", "delete-policy", "policy-name", add_option_dict)





