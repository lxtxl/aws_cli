#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/list-placements.html
if __name__ == '__main__':
    """
	create-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/create-placement.html
	delete-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/delete-placement.html
	describe-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/describe-placement.html
	update-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/update-placement.html
    """

    parameter_display_string = """
    # project-name : The project containing the placements to be listed.
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

    execute_one_parameter("iot1click-projects", "list-placements", "project-name", add_option_dict)