#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/clone-receipt-rule-set.html
if __name__ == '__main__':
    """
	create-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-receipt-rule-set.html
	delete-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-receipt-rule-set.html
	describe-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-receipt-rule-set.html
	list-receipt-rule-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-receipt-rule-sets.html
	reorder-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/reorder-receipt-rule-set.html
    """

    parameter_display_string = """
    # rule-set-name : The name of the rule set to create. The name must:

This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
Start and end with a letter or number.
Contain less than 64 characters.
    # original-rule-set-name : The name of the rule set to clone.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ses", "clone-receipt-rule-set", "rule-set-name", "original-rule-set-name", add_option_dict)
