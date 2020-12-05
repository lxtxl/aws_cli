#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoint.html
if __name__ == '__main__':
    """
	create-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-dev-endpoint.html
	delete-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-dev-endpoint.html
	get-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoints.html
	list-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-dev-endpoints.html
	update-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-dev-endpoint.html
    """

    parameter_display_string = """
    # endpoint-name : Name of the DevEndpoint to retrieve information for.
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

    execute_one_parameter("glue", "get-dev-endpoint", "endpoint-name", add_option_dict)