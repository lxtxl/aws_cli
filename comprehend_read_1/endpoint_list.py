#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-endpoint.html
if __name__ == '__main__':
    """
	create-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-endpoint.html
	delete-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-endpoint.html
	list-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-endpoints.html
	update-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/update-endpoint.html
    """

    parameter_display_string = """
    # endpoint-arn : The Amazon Resource Number (ARN) of the endpoint being described.
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

    execute_one_parameter("comprehend", "describe-endpoint", "endpoint-arn", add_option_dict)