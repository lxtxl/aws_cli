#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule-group.html
if __name__ == '__main__':
    """
	create-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule-group.html
	delete-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule-group.html
	list-rule-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rule-groups.html
	update-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule-group.html
    """

    parameter_display_string = """
    # rule-group-id : The RuleGroupId of the  RuleGroup that you want to get. RuleGroupId is returned by  CreateRuleGroup and by  ListRuleGroups .
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

    execute_one_parameter("waf", "get-rule-group", "rule-group-id", add_option_dict)