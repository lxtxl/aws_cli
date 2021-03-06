#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule.html
if __name__ == '__main__':
    """
	delete-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-topic-rule.html
	disable-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/disable-topic-rule.html
	enable-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/enable-topic-rule.html
	get-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-topic-rule.html
	list-topic-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-topic-rules.html
	replace-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/replace-topic-rule.html
    """

    parameter_display_string = """
    # rule-name : The name of the rule.
    # topic-rule-payload : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "create-topic-rule", "rule-name", "topic-rule-payload", add_option_dict)
