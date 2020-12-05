#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-public-key.html
if __name__ == '__main__':
    """
	create-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-public-key.html
	delete-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-public-key.html
	get-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-public-key.html
	list-public-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-public-keys.html
    """

    parameter_display_string = """
    # public-key-config : 
    # id : The identifier of the public key that you are updating.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudfront", "update-public-key", "public-key-config", "id", add_option_dict)
