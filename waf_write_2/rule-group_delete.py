#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule-group.html
if __name__ == '__main__':
    """
	create-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule-group.html
	get-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule-group.html
	list-rule-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rule-groups.html
	update-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule-group.html
    """

    parameter_display_string = """
    # rule-group-id : The RuleGroupId of the  RuleGroup that you want to delete. RuleGroupId is returned by  CreateRuleGroup and by  ListRuleGroups .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf", "delete-rule-group", "rule-group-id", "change-token", add_option_dict)
