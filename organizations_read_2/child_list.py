#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-children.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # parent-id : The unique identifier (ID) for the parent root or OU whose children you want to list.
The regex pattern for a parent ID string requires one of the following:

Root - A string that begins with âr-â followed by from 4 to 32 lowercase letters or digits.
Organizational unit (OU) - A string that begins with âou-â followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second â-â dash and from 8 to 32 additional lowercase letters or digits.
    # child-type : Filters the output to include only the specified child type.
Possible values:

ACCOUNT
ORGANIZATIONAL_UNIT
    """

    execute_two_parameter("organizations", "list-children", "parent-id", "child-type", parameter_display_string)