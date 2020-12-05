#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/reset-cache-parameter-group.html
if __name__ == '__main__':
    """
	create-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-parameter-group.html
	delete-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-parameter-group.html
	describe-cache-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-parameter-groups.html
	modify-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-parameter-group.html
    """

    parameter_display_string = """
    # cache-parameter-group-name : The name of the cache parameter group to reset.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "reset-cache-parameter-group", "cache-parameter-group-name", add_option_dict)





