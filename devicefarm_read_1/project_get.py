#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-project.html
if __name__ == '__main__':
    """
	create-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-project.html
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-projects.html
	update-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-project.html
    """

    parameter_display_string = """
    # arn : The projectâs ARN.
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

    execute_one_parameter("devicefarm", "get-project", "arn", add_option_dict)