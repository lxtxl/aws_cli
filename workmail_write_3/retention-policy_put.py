#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-retention-policy.html
if __name__ == '__main__':
    """
	delete-retention-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-retention-policy.html
    """

    parameter_display_string = """
    # organization-id : The organization ID.
    # name : The retention policy name.
    # folder-configurations : The retention policy folder configurations.
(structure)

The configuration applied to an organizationâs folders by its retention policy.
Name -> (string)

The folder name.

Action -> (string)

The action to take on the folder contents at the end of the folder configuration period.

Period -> (integer)

The period of time at which the folder configuration action is applied.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workmail", "put-retention-policy", "organization-id", "name", "folder-configurations", add_option_dict)
