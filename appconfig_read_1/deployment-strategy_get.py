#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-deployment-strategy.html
if __name__ == '__main__':
    """
	create-deployment-strategy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-deployment-strategy.html
	delete-deployment-strategy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-deployment-strategy.html
	list-deployment-strategies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-deployment-strategies.html
	update-deployment-strategy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-deployment-strategy.html
    """

    parameter_display_string = """
    # deployment-strategy-id : The ID of the deployment strategy to get.
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

    execute_one_parameter("appconfig", "get-deployment-strategy", "deployment-strategy-id", add_option_dict)