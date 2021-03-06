#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-rate-based-rule.html
if __name__ == '__main__':
    """
	create-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-rate-based-rule.html
	get-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-rate-based-rule.html
	list-rate-based-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-rate-based-rules.html
	update-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-rate-based-rule.html
    """

    parameter_display_string = """
    # rule-id : The RuleId of the  RateBasedRule that you want to delete. RuleId is returned by  CreateRateBasedRule and by  ListRateBasedRules .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf-regional", "delete-rate-based-rule", "rule-id", "change-token", add_option_dict)
