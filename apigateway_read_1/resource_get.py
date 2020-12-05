#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resources.html
if __name__ == '__main__':
    """
	create-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-resource.html
	delete-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-resource.html
	get-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resource.html
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/tag-resource.html
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/untag-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-resource.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
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

    execute_one_parameter("apigateway", "get-resources", "rest-api-id", add_option_dict)