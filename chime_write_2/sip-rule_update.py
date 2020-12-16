#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-sip-rule.html
if __name__ == '__main__':
    """
	create-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-sip-rule.html
	delete-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-sip-rule.html
	get-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-sip-rule.html
	list-sip-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-sip-rules.html
    """

    parameter_display_string = """
    # sip-rule-id : The SIP rule ID.
    # name : The new name for the specified SIP rule.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "update-sip-rule", "sip-rule-id", "name", add_option_dict)
