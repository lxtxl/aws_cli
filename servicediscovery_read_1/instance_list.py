#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html
if __name__ == '__main__':
    """
	deregister-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/deregister-instance.html
	discover-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html
	get-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html
	register-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/register-instance.html
    """

    parameter_display_string = """
    # service-id : The ID of the service that you want to list instances for.
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

    execute_one_parameter("servicediscovery", "list-instances", "service-id", add_option_dict)