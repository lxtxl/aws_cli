#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-alias.html
if __name__ == '__main__':
    """
	delete-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-alias.html
    """

    parameter_display_string = """
    # organization-id : The organization under which the member (user or group) exists.
    # entity-id : The member (user or group) to which this alias is added.
    # alias : The alias to add to the member set.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workmail", "create-alias", "organization-id", "entity-id", "alias", add_option_dict)
