#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/enable-rule.html
if __name__ == '__main__':
    """
	delete-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-rule.html
	describe-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-rule.html
	disable-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/disable-rule.html
	list-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rules.html
	put-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-rule.html
    """

    parameter_display_string = """
    # name : The name of the rule.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("events", "enable-rule", "name", add_option_dict)





