#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/put-permission-policy.html
if __name__ == '__main__':
    """
	delete-permission-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-permission-policy.html
	get-permission-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-permission-policy.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.
    # policy : The policy to attach to the specified RuleGroup.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf", "put-permission-policy", "resource-arn", "policy", add_option_dict)
