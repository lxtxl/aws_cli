#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-vocabulary.html
if __name__ == '__main__':
    """
	create-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-vocabulary.html
	delete-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary.html
	list-vocabularies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabularies.html
	update-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-vocabulary.html
    """

    parameter_display_string = """
    # vocabulary-name : The name of the vocabulary to return information about. The name is case sensitive.
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

    execute_one_parameter("transcribe", "get-vocabulary", "vocabulary-name", add_option_dict)