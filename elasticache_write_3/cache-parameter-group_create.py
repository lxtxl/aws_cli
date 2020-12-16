#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-parameter-group.html
if __name__ == '__main__':
    """
	delete-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-parameter-group.html
	describe-cache-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-parameter-groups.html
	modify-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-parameter-group.html
	reset-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/reset-cache-parameter-group.html
    """

    parameter_display_string = """
    # cache-parameter-group-name : A user-specified name for the cache parameter group.
    # cache-parameter-group-family : The name of the cache parameter group family that the cache parameter group can be used with.
Valid values are: memcached1.4 | memcached1.5 | memcached1.6 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 | redis6.x |
    # description : A user-specified description for the cache parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("elasticache", "create-cache-parameter-group", "cache-parameter-group-name", "cache-parameter-group-family", "description", add_option_dict)
