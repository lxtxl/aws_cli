#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-set.html
if __name__ == '__main__':
    """
	delete-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-set.html
	describe-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set.html
	list-stack-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-sets.html
	update-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-set.html
    """

    parameter_display_string = """
    # stack-set-name : The name to associate with the stack set. The name must be unique in the Region where you create your stack set.

Note
A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and canât be longer than 128 characters.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudformation", "create-stack-set", "stack-set-name", add_option_dict)





