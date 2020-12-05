#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-container-policy.html
if __name__ == '__main__':
    """
	delete-container-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-container-policy.html
	get-container-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-container-policy.html
    """

    parameter_display_string = """
    # container-name : The name of the container.
    # policy : The contents of the policy, which includes the following:

One Version tag
One Statement tag that contains the standard tags for the policy.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediastore", "put-container-policy", "container-name", "policy", add_option_dict)
