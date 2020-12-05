#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-byte-match-set.html
if __name__ == '__main__':
    """
	delete-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-byte-match-set.html
	get-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-byte-match-set.html
	list-byte-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-byte-match-sets.html
	update-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-byte-match-set.html
    """

    parameter_display_string = """
    # name : A friendly name or description of the  ByteMatchSet . You canât change Name after you create a ByteMatchSet .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf-regional", "create-byte-match-set", "name", "change-token", add_option_dict)
