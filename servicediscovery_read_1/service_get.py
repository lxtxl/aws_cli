#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html
if __name__ == '__main__':
    """
	create-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-service.html
	delete-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/delete-service.html
	list-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-services.html
	update-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html
    """

    parameter_display_string = """
    # id : The ID of the service that you want to get settings for.
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

    execute_one_parameter("servicediscovery", "get-service", "id", add_option_dict)