#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule.html
if __name__ == '__main__':
    """
	create-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule.html
	get-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule.html
	list-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rules.html
	update-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule.html
    """

    parameter_display_string = """
    # rule-id : The RuleId of the  Rule that you want to delete. RuleId is returned by  CreateRule and by  ListRules .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf", "delete-rule", "rule-id", "change-token", add_option_dict)
