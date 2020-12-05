#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/detach-typed-link.html
if __name__ == '__main__':
    """
	attach-typed-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/attach-typed-link.html
    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) of the directory where you want to detach the typed link.
    # typed-link-specifier : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "detach-typed-link", "directory-arn", "typed-link-specifier", add_option_dict)
