#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-policy.html
if __name__ == '__main__':
    """
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-policy.html
	get-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-policies.html
    """

    parameter_display_string = """
    # policy : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("fms", "put-policy", "policy", add_option_dict)





