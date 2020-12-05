#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-key-group.html
if __name__ == '__main__':
    """
	create-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-key-group.html
	delete-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-key-group.html
	get-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-key-group.html
	list-key-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-key-groups.html
    """

    parameter_display_string = """
    # key-group-config : 
    # id : The identifier of the key group that you are updating.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudfront", "update-key-group", "key-group-config", "id", add_option_dict)
