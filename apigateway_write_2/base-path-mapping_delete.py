#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-base-path-mapping.html
if __name__ == '__main__':
    """
	create-base-path-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-base-path-mapping.html
	get-base-path-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-base-path-mapping.html
	get-base-path-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-base-path-mappings.html
	update-base-path-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-base-path-mapping.html
    """

    parameter_display_string = """
    # domain-name : [Required] The domain name of the  BasePathMapping resource to delete.
    # base-path : [Required] The base path name of the  BasePathMapping resource to delete.
To specify an empty base path, set this parameter to '(none)' .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "delete-base-path-mapping", "domain-name", "base-path", add_option_dict)
