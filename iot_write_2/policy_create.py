#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy.html
if __name__ == '__main__':
    """
	attach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-policy.html
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy.html
	detach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-policy.html
	get-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policies.html
    """

    parameter_display_string = """
    # policy-name : The policy name.
    # policy-document : The JSON document that describes the policy. policyDocument must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "create-policy", "policy-name", "policy-document", add_option_dict)
