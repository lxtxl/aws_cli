#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-key.html
if __name__ == '__main__':
    """
	create-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-api-key.html
	delete-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-api-key.html
	get-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-keys.html
	import-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-api-keys.html
	update-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-api-key.html
    """

    parameter_display_string = """
    # api-key : [Required] The identifier of the  ApiKey resource.
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

    execute_one_parameter("apigateway", "get-api-key", "api-key", add_option_dict)