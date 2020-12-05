#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/lookup-policy.html
if __name__ == '__main__':
    """
	attach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/attach-policy.html
	detach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/detach-policy.html
    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory . For more information, see  arns .
    # object-reference : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "lookup-policy", "directory-arn", "object-reference", add_option_dict)
