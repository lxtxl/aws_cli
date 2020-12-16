#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-option-group.html
if __name__ == '__main__':
    """
	create-option-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-option-group.html
	delete-option-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-option-group.html
	describe-option-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-option-groups.html
    """

    parameter_display_string = """
    # source-option-group-identifier : The identifier for the source option group.
Constraints:

Must specify a valid option group.
    # target-option-group-identifier : The identifier for the copied option group.
Constraints:

Canât be null, empty, or blank
Must contain from 1 to 255 letters, numbers, or hyphens
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens

Example: my-option-group
    # target-option-group-description : The description for the copied option group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "copy-option-group", "source-option-group-identifier", "target-option-group-identifier", "target-option-group-description", add_option_dict)
