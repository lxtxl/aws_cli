#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-pattern-set.html
if __name__ == '__main__':
    """
	delete-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-regex-pattern-set.html
	get-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-regex-pattern-set.html
	list-regex-pattern-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-regex-pattern-sets.html
	update-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-regex-pattern-set.html
    """

    parameter_display_string = """
    # name : A friendly name or description of the  RegexPatternSet . You canât change Name after you create a RegexPatternSet .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf", "create-regex-pattern-set", "name", "change-token", add_option_dict)
