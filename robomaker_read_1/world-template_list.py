#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-world-template.html
if __name__ == '__main__':
    """
	create-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-world-template.html
	delete-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-world-template.html
	list-world-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-world-templates.html
	update-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-world-template.html
    """

    parameter_display_string = """
    # template : The Amazon Resource Name (arn) of the world template you want to describe.
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

    execute_one_parameter("robomaker", "describe-world-template", "template", add_option_dict)