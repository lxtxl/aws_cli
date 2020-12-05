#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-services.html
if __name__ == '__main__':
    """
	create-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html
	delete-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-service.html
	list-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-services.html
	update-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html
    """

    parameter_display_string = """
    # services : A list of services to describe. You may specify up to 10 services to describe in a single operation.
(string)
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

    execute_one_parameter("ecs", "describe-services", "services", add_option_dict)