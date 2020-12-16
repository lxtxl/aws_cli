#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-sip-rule.html
if __name__ == '__main__':
    """
	create-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-sip-rule.html
	delete-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-sip-rule.html
	list-sip-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-sip-rules.html
	update-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-sip-rule.html
    """

    parameter_display_string = """
    # sip-rule-id : The SIP rule ID.
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

    execute_one_parameter("chime", "get-sip-rule", "sip-rule-id", add_option_dict)