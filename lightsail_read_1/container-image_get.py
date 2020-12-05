#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-images.html
if __name__ == '__main__':
    """
	delete-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-container-image.html
	push-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/push-container-image.html
	register-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/register-container-image.html
    """

    parameter_display_string = """
    # service-name : The name of the container service for which to return registered container images.
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

    execute_one_parameter("lightsail", "get-container-images", "service-name", add_option_dict)