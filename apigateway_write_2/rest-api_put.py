#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-rest-api.html
if __name__ == '__main__':
    """
	create-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-rest-api.html
	delete-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-rest-api.html
	get-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-rest-api.html
	get-rest-apis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-rest-apis.html
	import-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-rest-api.html
	update-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-rest-api.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # body : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "put-rest-api", "rest-api-id", "body", add_option_dict)
