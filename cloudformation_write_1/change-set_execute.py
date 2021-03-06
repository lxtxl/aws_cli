#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/execute-change-set.html
if __name__ == '__main__':
    """
	create-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-change-set.html
	delete-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-change-set.html
	describe-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-change-set.html
	list-change-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-change-sets.html
    """

    parameter_display_string = """
    # change-set-name : The name or ARN of the change set that you want use to update the specified stack.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudformation", "execute-change-set", "change-set-name", add_option_dict)





