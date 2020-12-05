#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-byte-match-set.html
if __name__ == '__main__':
    """
	create-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-byte-match-set.html
	delete-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-byte-match-set.html
	list-byte-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-byte-match-sets.html
	update-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-byte-match-set.html
    """

    parameter_display_string = """
    # byte-match-set-id : The ByteMatchSetId of the  ByteMatchSet that you want to get. ByteMatchSetId is returned by  CreateByteMatchSet and by  ListByteMatchSets .
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

    execute_one_parameter("waf", "get-byte-match-set", "byte-match-set-id", add_option_dict)