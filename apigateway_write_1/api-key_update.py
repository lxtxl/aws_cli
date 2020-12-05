#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-api-key.html
if __name__ == '__main__':
    """
	create-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-api-key.html
	delete-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-api-key.html
	get-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-key.html
	get-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-keys.html
	import-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-api-keys.html
    """

    parameter_display_string = """
    # api-key : [Required] The identifier of the  ApiKey resource to be updated.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("apigateway", "update-api-key", "api-key", add_option_dict)





