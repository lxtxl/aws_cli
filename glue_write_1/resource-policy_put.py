#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/put-resource-policy.html
if __name__ == '__main__':
    """
	delete-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-resource-policy.html
	get-resource-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-resource-policies.html
	get-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-resource-policy.html
    """

    parameter_display_string = """
    # policy-in-json : Contains the policy document to set, in JSON format.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "put-resource-policy", "policy-in-json", add_option_dict)





