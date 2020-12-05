#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-model.html
if __name__ == '__main__':
    """
	create-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-model.html
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-model.html
	get-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-model.html
	get-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-models.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # model-name : [Required] The name of the model to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "update-model", "rest-api-id", "model-name", add_option_dict)
