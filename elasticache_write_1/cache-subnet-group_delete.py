#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-subnet-group.html
if __name__ == '__main__':
    """
	create-cache-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-subnet-group.html
	describe-cache-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-subnet-groups.html
	modify-cache-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-subnet-group.html
    """

    parameter_display_string = """
    # cache-subnet-group-name : The name of the cache subnet group to delete.
Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "delete-cache-subnet-group", "cache-subnet-group-name", add_option_dict)





