#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-insight-rule.html
if __name__ == '__main__':
    """
	delete-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-insight-rules.html
	describe-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-insight-rules.html
	disable-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/disable-insight-rules.html
	enable-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/enable-insight-rules.html
    """

    parameter_display_string = """
    # rule-name : A unique name for the rule.
    # rule-definition : The definition of the rule, as a JSON object. For details on the valid syntax, see Contributor Insights Rule Syntax .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudwatch", "put-insight-rule", "rule-name", "rule-definition", add_option_dict)
