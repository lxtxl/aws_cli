#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-medical-vocabulary.html
if __name__ == '__main__':
    """
	create-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-medical-vocabulary.html
	get-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-vocabulary.html
	list-medical-vocabularies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-medical-vocabularies.html
	update-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-medical-vocabulary.html
    """

    parameter_display_string = """
    # vocabulary-name : The name of the vocabulary that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("transcribe", "delete-medical-vocabulary", "vocabulary-name", add_option_dict)





