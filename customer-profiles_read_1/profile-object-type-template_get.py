#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-profile-object-type-template.html
if __name__ == '__main__':
    """
	list-profile-object-type-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-profile-object-type-templates.html
    """

    parameter_display_string = """
    # template-id : A unique identifier for the object template.
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

    execute_one_parameter("customer-profiles", "get-profile-object-type-template", "template-id", add_option_dict)