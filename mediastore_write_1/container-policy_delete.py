#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-container-policy.html
if __name__ == '__main__':
    """
	get-container-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-container-policy.html
	put-container-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-container-policy.html
    """

    parameter_display_string = """
    # container-name : The name of the container that holds the policy.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediastore", "delete-container-policy", "container-name", add_option_dict)





