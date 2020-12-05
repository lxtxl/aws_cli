#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-image-permissions.html
if __name__ == '__main__':
    """
	delete-image-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-image-permissions.html
	update-image-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-image-permissions.html
    """

    parameter_display_string = """
    # name : The name of the private image for which to describe permissions. The image must be one that you own.
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

    execute_one_parameter("appstream", "describe-image-permissions", "name", add_option_dict)