#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-rest-api.html
if __name__ == '__main__':
    """
	create-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-rest-api.html
	delete-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-rest-api.html
	get-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-rest-api.html
	get-rest-apis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-rest-apis.html
	import-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-rest-api.html
	put-rest-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-rest-api.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("apigateway", "update-rest-api", "rest-api-id", add_option_dict)





