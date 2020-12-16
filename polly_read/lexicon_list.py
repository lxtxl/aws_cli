#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/list-lexicons.html
if __name__ == '__main__':
    """
	delete-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/delete-lexicon.html
	get-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-lexicon.html
	put-lexicon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/put-lexicon.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("polly", "list-lexicons", add_option_dict)