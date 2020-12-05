#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-resource.html
if __name__ == '__main__':
    """
	create-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-resource.html
	get-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resource.html
	get-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resources.html
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/tag-resource.html
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/untag-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-resource.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # resource-id : [Required] The identifier of the  Resource resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "delete-resource", "rest-api-id", "resource-id", add_option_dict)
