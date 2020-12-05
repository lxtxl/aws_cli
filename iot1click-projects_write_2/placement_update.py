#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/update-placement.html
if __name__ == '__main__':
    """
	create-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/create-placement.html
	delete-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/delete-placement.html
	describe-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/describe-placement.html
	list-placements : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/list-placements.html
    """

    parameter_display_string = """
    # placement-name : The name of the placement to update.
    # project-name : The name of the project containing the placement to be updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot1click-projects", "update-placement", "placement-name", "project-name", add_option_dict)
