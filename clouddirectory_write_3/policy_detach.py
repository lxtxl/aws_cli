#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/detach-policy.html
if __name__ == '__main__':
    """
	attach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/attach-policy.html
	lookup-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/lookup-policy.html
    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory where both objects reside. For more information, see  arns .
    # policy-reference : 
    # object-reference : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("clouddirectory", "detach-policy", "directory-arn", "policy-reference", "object-reference", add_option_dict)
