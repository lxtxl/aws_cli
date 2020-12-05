#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-permission-policy.html
if __name__ == '__main__':
    """
	get-permission-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-permission-policy.html
	put-permission-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/put-permission-policy.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the RuleGroup from which you want to delete the policy.
The user making the request must be the owner of the RuleGroup.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("waf", "delete-permission-policy", "resource-arn", add_option_dict)





