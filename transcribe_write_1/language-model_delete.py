#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-language-model.html
if __name__ == '__main__':
    """
	create-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-language-model.html
	describe-language-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/describe-language-model.html
	list-language-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-language-models.html
    """

    parameter_display_string = """
    # model-name : The name of the model youâre choosing to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("transcribe", "delete-language-model", "model-name", add_option_dict)





