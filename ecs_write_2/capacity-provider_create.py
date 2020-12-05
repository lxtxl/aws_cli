#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-capacity-provider.html
if __name__ == '__main__':
    """
	delete-capacity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-capacity-provider.html
	describe-capacity-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-capacity-providers.html
    """

    parameter_display_string = """
    # name : The name of the capacity provider. Up to 255 characters are allowed, including letters (upper and lowercase), numbers, underscores, and hyphens. The name cannot be prefixed with âaws â, âecs â, or âfargate â.
    # auto-scaling-group-provider : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecs", "create-capacity-provider", "name", "auto-scaling-group-provider", add_option_dict)
