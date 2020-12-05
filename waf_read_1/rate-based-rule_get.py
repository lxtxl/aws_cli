#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rate-based-rule.html
if __name__ == '__main__':
    """
	create-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rate-based-rule.html
	delete-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rate-based-rule.html
	list-rate-based-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rate-based-rules.html
	update-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rate-based-rule.html
    """

    parameter_display_string = """
    # rule-id : The RuleId of the  RateBasedRule that you want to get. RuleId is returned by  CreateRateBasedRule and by  ListRateBasedRules .
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("waf", "get-rate-based-rule", "rule-id", add_option_dict)