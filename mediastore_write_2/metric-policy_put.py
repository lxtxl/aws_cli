#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-metric-policy.html
if __name__ == '__main__':
    """
	delete-metric-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-metric-policy.html
	get-metric-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-metric-policy.html
    """

    parameter_display_string = """
    # container-name : The name of the container that you want to add the metric policy to.
    # metric-policy : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediastore", "put-metric-policy", "container-name", "metric-policy", add_option_dict)
