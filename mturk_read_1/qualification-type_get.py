#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-qualification-type.html
if __name__ == '__main__':
    """
	create-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-qualification-type.html
	delete-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/delete-qualification-type.html
	list-qualification-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-qualification-types.html
	update-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/update-qualification-type.html
    """

    parameter_display_string = """
    # qualification-type-id : The ID of the QualificationType.
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

    execute_one_parameter("mturk", "get-qualification-type", "qualification-type-id", add_option_dict)