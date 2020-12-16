#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-subnet-group.html
if __name__ == '__main__':
    """
	delete-cache-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-subnet-group.html
	describe-cache-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-subnet-groups.html
	modify-cache-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-subnet-group.html
    """

    parameter_display_string = """
    # cache-subnet-group-name : A name for the cache subnet group. This value is stored as a lowercase string.
Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
Example: mysubnetgroup
    # cache-subnet-group-description : A description for the cache subnet group.
    # subnet-ids : A list of VPC subnet IDs for the cache subnet group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("elasticache", "create-cache-subnet-group", "cache-subnet-group-name", "cache-subnet-group-description", "subnet-ids", add_option_dict)
