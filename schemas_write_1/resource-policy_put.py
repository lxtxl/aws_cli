#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/put-resource-policy.html
if __name__ == '__main__':
    """
	delete-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-resource-policy.html
	get-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/get-resource-policy.html
    """

    parameter_display_string = """
    # policy : The resource-based policy.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("schemas", "put-resource-policy", "policy", add_option_dict)





