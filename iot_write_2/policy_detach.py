#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-policy.html
if __name__ == '__main__':
    """
	attach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-policy.html
	create-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy.html
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy.html
	get-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policies.html
    """

    parameter_display_string = """
    # policy-name : The policy to detach.
    # target : The target from which the policy will be detached.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "detach-policy", "policy-name", "target", add_option_dict)
