#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-security-group.html
if __name__ == '__main__':
    """
	delete-cache-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-security-group.html
	describe-cache-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-security-groups.html
    """

    parameter_display_string = """
    # cache-security-group-name : A name for the cache security group. This value is stored as a lowercase string.
Constraints: Must contain no more than 255 alphanumeric characters. Cannot be the word âDefaultâ.
Example: mysecuritygroup
    # description : A description for the cache security group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "create-cache-security-group", "cache-security-group-name", "description", add_option_dict)
