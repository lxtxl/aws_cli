#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/delete-lexicon.html
if __name__ == '__main__':
    """
	get-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-lexicon.html
	list-lexicons : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/list-lexicons.html
	put-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/put-lexicon.html
    """

    parameter_display_string = """
    # name : The name of the lexicon to delete. Must be an existing lexicon in the region.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("polly", "delete-lexicon", "name", add_option_dict)





