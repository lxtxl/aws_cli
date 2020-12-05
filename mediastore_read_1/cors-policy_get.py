#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-cors-policy.html
if __name__ == '__main__':
    """
	delete-cors-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-cors-policy.html
	put-cors-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-cors-policy.html
    """

    parameter_display_string = """
    # container-name : The name of the container that the policy is assigned to.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("mediastore", "get-cors-policy", "container-name", add_option_dict)