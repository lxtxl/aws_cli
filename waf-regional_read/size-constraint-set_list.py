#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-size-constraint-sets.html
if __name__ == '__main__':
    """
	create-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-size-constraint-set.html
	delete-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-size-constraint-set.html
	get-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-size-constraint-set.html
	update-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-size-constraint-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("waf-regional", "list-size-constraint-sets", add_option_dict)