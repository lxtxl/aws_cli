#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-permission-policy.html
if __name__ == '__main__':
    """
	get-permission-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-permission-policy.html
	put-permission-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/put-permission-policy.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the rule group from which you want to delete the policy.
You must be the owner of the rule group to perform this operation.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("wafv2", "delete-permission-policy", "resource-arn", add_option_dict)





