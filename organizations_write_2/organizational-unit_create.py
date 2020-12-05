#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organizational-unit.html
if __name__ == '__main__':
    """
	delete-organizational-unit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organizational-unit.html
	describe-organizational-unit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-organizational-unit.html
	update-organizational-unit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/update-organizational-unit.html
    """

    parameter_display_string = """
    # parent-id : The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
The regex pattern for a parent ID string requires one of the following:

Root - A string that begins with âr-â followed by from 4 to 32 lowercase letters or digits.
Organizational unit (OU) - A string that begins with âou-â followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second â-â dash and from 8 to 32 additional lowercase letters or digits.
    # name : The friendly name to assign to the new OU.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "create-organizational-unit", "parent-id", "name", add_option_dict)
