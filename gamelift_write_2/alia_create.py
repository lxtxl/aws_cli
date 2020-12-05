#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-alias.html
if __name__ == '__main__':
    """
	delete-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-alias.html
	describe-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-alias.html
	resolve-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/resolve-alias.html
	update-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-alias.html
    """

    parameter_display_string = """
    # name : A descriptive label that is associated with an alias. Alias names do not need to be unique.
    # routing-strategy : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "create-alias", "name", "routing-strategy", add_option_dict)
