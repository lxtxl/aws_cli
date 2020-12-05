#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-request-validator.html
if __name__ == '__main__':
    """
	delete-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-request-validator.html
	get-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-request-validator.html
	get-request-validators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-request-validators.html
	update-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-request-validator.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("apigateway", "create-request-validator", "rest-api-id", add_option_dict)





