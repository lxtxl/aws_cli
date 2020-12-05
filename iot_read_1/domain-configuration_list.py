#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html
if __name__ == '__main__':
    """
	create-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-domain-configuration.html
	delete-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-domain-configuration.html
	list-domain-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-domain-configurations.html
	update-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-domain-configuration.html
    """

    parameter_display_string = """
    # domain-configuration-name : The name of the domain configuration.
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

    execute_one_parameter("iot", "describe-domain-configuration", "domain-configuration-name", add_option_dict)