#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoints.html
if __name__ == '__main__':
    """
	create-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-dev-endpoint.html
	delete-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-dev-endpoint.html
	get-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoint.html
	list-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-dev-endpoints.html
	update-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-dev-endpoint.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("glue", "get-dev-endpoints", add_option_dict)