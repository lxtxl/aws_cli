#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/put-lexicon.html
if __name__ == '__main__':
    """
	delete-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/delete-lexicon.html
	get-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-lexicon.html
	list-lexicons : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/list-lexicons.html
    """

    parameter_display_string = """
    # name : Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long.
    # content : Content of the PLS lexicon as string data.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("polly", "put-lexicon", "name", "content", add_option_dict)
