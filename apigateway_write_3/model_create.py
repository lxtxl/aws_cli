#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-model.html
if __name__ == '__main__':
    """
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-model.html
	get-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-model.html
	get-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-models.html
	update-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-model.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The  RestApi identifier under which the  Model will be created.
    # name : [Required] The name of the model. Must be alphanumeric.
    # content-type : [Required] The content-type for the model.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigateway", "create-model", "rest-api-id", "name", "content-type", add_option_dict)
