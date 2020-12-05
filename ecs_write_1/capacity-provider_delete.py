#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-capacity-provider.html
if __name__ == '__main__':
    """
	create-capacity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-capacity-provider.html
	describe-capacity-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-capacity-providers.html
    """

    parameter_display_string = """
    # capacity-provider : The short name or full Amazon Resource Name (ARN) of the capacity provider to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "delete-capacity-provider", "capacity-provider", add_option_dict)





