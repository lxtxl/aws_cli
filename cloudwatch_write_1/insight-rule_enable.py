#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/enable-insight-rules.html
if __name__ == '__main__':
    """
	delete-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-insight-rules.html
	describe-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-insight-rules.html
	disable-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/disable-insight-rules.html
	put-insight-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-insight-rule.html
    """

    parameter_display_string = """
    # rule-names : An array of the rule names to enable. If you need to find out the names of your rules, use DescribeInsightRules .
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudwatch", "enable-insight-rules", "rule-names", add_option_dict)





