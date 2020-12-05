#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/describe-language-model.html
if __name__ == '__main__':
    """
	create-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-language-model.html
	delete-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-language-model.html
	list-language-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-language-models.html
    """

    parameter_display_string = """
    # model-name : The name of the custom language model you submit to get more information.
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

    execute_one_parameter("transcribe", "describe-language-model", "model-name", add_option_dict)