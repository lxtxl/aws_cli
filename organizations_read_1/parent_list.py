#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-parents.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # child-id : The unique identifier (ID) of the OU or account whose parent containers you want to list. Donât specify a root.
The regex pattern for a child ID string requires one of the following:

Account - A string that consists of exactly 12 digits.
Organizational unit (OU) - A string that begins with âou-â followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second â-â dash and from 8 to 32 additional lowercase letters or digits.
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

    execute_one_parameter("organizations", "list-parents", "child-id", add_option_dict)