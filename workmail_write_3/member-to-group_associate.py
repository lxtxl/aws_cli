#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/associate-member-to-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The organization under which the group exists.
    # group-id : The group to which the member (user or group) is associated.
    # member-id : The member (user or group) to associate to the group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workmail", "associate-member-to-group", "organization-id", "group-id", "member-id", add_option_dict)
