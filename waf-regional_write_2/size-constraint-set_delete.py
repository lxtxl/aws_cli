#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-size-constraint-set.html
if __name__ == '__main__':
    """
	create-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-size-constraint-set.html
	get-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-size-constraint-set.html
	list-size-constraint-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-size-constraint-sets.html
	update-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-size-constraint-set.html
    """

    parameter_display_string = """
    # size-constraint-set-id : The SizeConstraintSetId of the  SizeConstraintSet that you want to delete. SizeConstraintSetId is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf-regional", "delete-size-constraint-set", "size-constraint-set-id", "change-token", add_option_dict)
