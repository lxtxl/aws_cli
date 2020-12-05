#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-lifecycle-policy.html
if __name__ == '__main__':
    """
	delete-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-lifecycle-policy.html
	get-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-lifecycle-policy.html
    """

    parameter_display_string = """
    # container-name : The name of the container that you want to assign the object lifecycle policy to.
    # lifecycle-policy : The object lifecycle policy to apply to the container.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediastore", "put-lifecycle-policy", "container-name", "lifecycle-policy", add_option_dict)
