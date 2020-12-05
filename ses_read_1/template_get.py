#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-template.html
if __name__ == '__main__':
    """
	create-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-template.html
	delete-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-template.html
	list-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-templates.html
	update-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/update-template.html
    """

    parameter_display_string = """
    # template-name : The name of the template you want to retrieve.
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

    execute_one_parameter("ses", "get-template", "template-name", add_option_dict)