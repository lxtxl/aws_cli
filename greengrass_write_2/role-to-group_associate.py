#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/associate-role-to-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # group-id : The ID of the Greengrass group.
    # role-arn : The ARN of the role you wish to associate with this group. The existence of the role is not validated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("greengrass", "associate-role-to-group", "group-id", "role-arn", add_option_dict)
