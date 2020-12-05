#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-size-constraint-set.html
if __name__ == '__main__':
    """
	delete-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-size-constraint-set.html
	get-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-size-constraint-set.html
	list-size-constraint-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-size-constraint-sets.html
	update-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-size-constraint-set.html
    """

    parameter_display_string = """
    # name : A friendly name or description of the  SizeConstraintSet . You canât change Name after you create a SizeConstraintSet .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf-regional", "create-size-constraint-set", "name", "change-token", add_option_dict)
