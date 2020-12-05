#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-security-group.html
if __name__ == '__main__':
    """
	create-cache-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-security-group.html
	describe-cache-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-security-groups.html
    """

    parameter_display_string = """
    # cache-security-group-name : The name of the cache security group to delete.

Note
You cannot delete the default security group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "delete-cache-security-group", "cache-security-group-name", add_option_dict)





