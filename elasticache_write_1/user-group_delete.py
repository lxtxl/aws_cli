#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-user-group.html
if __name__ == '__main__':
    """
	create-user-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-user-group.html
	describe-user-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-user-groups.html
	modify-user-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-user-group.html
    """

    parameter_display_string = """
    # user-group-id : The ID of the user group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "delete-user-group", "user-group-id", add_option_dict)





