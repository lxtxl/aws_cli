#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-sip-rules.html
if __name__ == '__main__':
    """
	create-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-sip-rule.html
	delete-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-sip-rule.html
	get-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-sip-rule.html
	update-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-sip-rule.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("chime", "list-sip-rules", add_option_dict)