#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-alias.html
if __name__ == '__main__':
    """
	create-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-alias.html
    """

    parameter_display_string = """
    # organization-id : The identifier for the organization under which the user exists.
    # entity-id : The identifier for the member (user or group) from which to have the aliases removed.
    # alias : The aliases to be removed from the userâs set of aliases. Duplicate entries in the list are collapsed into single entries (the list is transformed into a set).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workmail", "delete-alias", "organization-id", "entity-id", "alias", add_option_dict)
