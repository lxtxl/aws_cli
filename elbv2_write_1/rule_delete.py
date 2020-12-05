#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-rule.html
if __name__ == '__main__':
    """
	create-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-rule.html
	describe-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-rules.html
	modify-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-rule.html
    """

    parameter_display_string = """
    # rule-arn : The Amazon Resource Name (ARN) of the rule.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elbv2", "delete-rule", "rule-arn", add_option_dict)




