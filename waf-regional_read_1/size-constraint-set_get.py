#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-size-constraint-set.html
if __name__ == '__main__':
    """
	create-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-size-constraint-set.html
	delete-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-size-constraint-set.html
	list-size-constraint-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-size-constraint-sets.html
	update-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-size-constraint-set.html
    """

    parameter_display_string = """
    # size-constraint-set-id : The SizeConstraintSetId of the  SizeConstraintSet that you want to get. SizeConstraintSetId is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .
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

    execute_one_parameter("waf-regional", "get-size-constraint-set", "size-constraint-set-id", add_option_dict)