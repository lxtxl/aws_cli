#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-option-group.html
if __name__ == '__main__':
    """
	copy-option-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-option-group.html
	create-option-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-option-group.html
	describe-option-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-option-groups.html
    """

    parameter_display_string = """
    # option-group-name : The name of the option group to be deleted.

Note
You canât delete default option groups.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "delete-option-group", "option-group-name", add_option_dict)





