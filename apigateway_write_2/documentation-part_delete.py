#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-documentation-part.html
if __name__ == '__main__':
    """
	create-documentation-part : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-documentation-part.html
	get-documentation-part : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-documentation-part.html
	get-documentation-parts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-documentation-parts.html
	import-documentation-parts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-documentation-parts.html
	update-documentation-part : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-documentation-part.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # documentation-part-id : [Required] The identifier of the to-be-deleted documentation part.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "delete-documentation-part", "rest-api-id", "documentation-part-id", add_option_dict)
