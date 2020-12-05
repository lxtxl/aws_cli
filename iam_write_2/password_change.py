#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/change-password.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # old-password : The IAM userâs current password.
    # new-password : The new password. The new password must conform to the AWS accountâs password policy, if one exists.
The regex pattern that is used to validate this parameter is a string of characters. That string can include almost any printable ASCII character from the space (\u0020 ) through the end of the ASCII character range (\u00FF ). You can also include the tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D ) characters. Any of these characters are valid in a password. However, many tools, such as the AWS Management Console, might restrict the ability to type certain characters because they have special meaning within that tool.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "change-password", "old-password", "new-password", add_option_dict)
