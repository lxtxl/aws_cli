#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-container-instances.html
if __name__ == '__main__':
    """
	deregister-container-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deregister-container-instance.html
	list-container-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-container-instances.html
	register-container-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-container-instance.html
    """

    parameter_display_string = """
    # container-instances : A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.
(string)
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

    execute_one_parameter("ecs", "describe-container-instances", "container-instances", add_option_dict)