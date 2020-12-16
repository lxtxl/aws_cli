#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-language-models.html
if __name__ == '__main__':
    """
	create-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-language-model.html
	delete-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-language-model.html
	describe-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/describe-language-model.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("transcribe", "list-language-models", add_option_dict)