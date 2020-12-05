#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-fleet.html
if __name__ == '__main__':
    """
	delete-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-fleet.html
	describe-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-fleet.html
	list-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-fleets.html
    """

    parameter_display_string = """
    # name : The name of the fleet.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "create-fleet", "name", add_option_dict)





