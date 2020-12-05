#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-regex-match-set.html
if __name__ == '__main__':
    """
	create-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-match-set.html
	delete-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-regex-match-set.html
	list-regex-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-regex-match-sets.html
	update-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-regex-match-set.html
    """

    parameter_display_string = """
    # regex-match-set-id : The RegexMatchSetId of the  RegexMatchSet that you want to get. RegexMatchSetId is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .
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

    execute_one_parameter("waf", "get-regex-match-set", "regex-match-set-id", add_option_dict)