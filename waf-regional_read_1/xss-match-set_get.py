#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-xss-match-set.html
if __name__ == '__main__':
    """
	create-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-xss-match-set.html
	delete-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-xss-match-set.html
	list-xss-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-xss-match-sets.html
	update-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-xss-match-set.html
    """

    parameter_display_string = """
    # xss-match-set-id : The XssMatchSetId of the  XssMatchSet that you want to get. XssMatchSetId is returned by  CreateXssMatchSet and by  ListXssMatchSets .
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

    execute_one_parameter("waf-regional", "get-xss-match-set", "xss-match-set-id", add_option_dict)