#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-intents.html
if __name__ == '__main__':
    """
	delete-intent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-intent.html
	get-intent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-intent.html
	put-intent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-intent.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("lex-models", "get-intents", add_option_dict)