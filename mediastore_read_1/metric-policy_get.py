#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-metric-policy.html
if __name__ == '__main__':
    """
	delete-metric-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-metric-policy.html
	put-metric-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-metric-policy.html
    """

    parameter_display_string = """
    # container-name : The name of the container that is associated with the metric policy.
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

    execute_one_parameter("mediastore", "get-metric-policy", "container-name", add_option_dict)