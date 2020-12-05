#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-regex-pattern-set.html
if __name__ == '__main__':
    """
	create-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-regex-pattern-set.html
	delete-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-regex-pattern-set.html
	list-regex-pattern-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-regex-pattern-sets.html
	update-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-regex-pattern-set.html
    """

    parameter_display_string = """
    # regex-pattern-set-id : The RegexPatternSetId of the  RegexPatternSet that you want to get. RegexPatternSetId is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
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

    execute_one_parameter("waf-regional", "get-regex-pattern-set", "regex-pattern-set-id", add_option_dict)