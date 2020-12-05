#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-vocabulary-filter.html
if __name__ == '__main__':
    """
	create-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-vocabulary-filter.html
	delete-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary-filter.html
	get-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-vocabulary-filter.html
	list-vocabulary-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabulary-filters.html
    """

    parameter_display_string = """
    # vocabulary-filter-name : The name of the vocabulary filter to update. If you try to update a vocabulary filter with the same name as another vocabulary filter, you get a ConflictException error.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("transcribe", "update-vocabulary-filter", "vocabulary-filter-name", add_option_dict)





