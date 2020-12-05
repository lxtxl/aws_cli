#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/untag.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # arn : The ARN of the resource group from which to remove tags. The command removed both the specified keys and any values associated with those keys.
    # keys : The keys of the tags to be removed.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("resource-groups", "untag", "arn", "keys", add_option_dict)
