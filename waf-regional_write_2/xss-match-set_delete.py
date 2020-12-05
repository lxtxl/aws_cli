#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-xss-match-set.html
if __name__ == '__main__':
    """
	create-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-xss-match-set.html
	get-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-xss-match-set.html
	list-xss-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-xss-match-sets.html
	update-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-xss-match-set.html
    """

    parameter_display_string = """
    # xss-match-set-id : The XssMatchSetId of the  XssMatchSet that you want to delete. XssMatchSetId is returned by  CreateXssMatchSet and by  ListXssMatchSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf-regional", "delete-xss-match-set", "xss-match-set-id", "change-token", add_option_dict)
