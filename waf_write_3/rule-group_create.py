#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule-group.html
if __name__ == '__main__':
    """
	delete-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule-group.html
	get-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule-group.html
	list-rule-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rule-groups.html
	update-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule-group.html
    """

    parameter_display_string = """
    # name : A friendly name or description of the  RuleGroup . You canât change Name after you create a RuleGroup .
    # metric-name : A friendly name or description for the metrics for this RuleGroup . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It canât contain whitespace or metric names reserved for AWS WAF, including âAllâ and âDefault_Action.â You canât change the name of the metric after you create the RuleGroup .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf", "create-rule-group", "name", "metric-name", "change-token", add_option_dict)
