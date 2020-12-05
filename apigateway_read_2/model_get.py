#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-model.html
if __name__ == '__main__':
    """
	create-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-model.html
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-model.html
	get-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-models.html
	update-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-model.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The  RestApi identifier under which the  Model exists.
    # model-name : [Required] The name of the model as an identifier.
    """

    execute_two_parameter("apigateway", "get-model", "rest-api-id", "model-name", parameter_display_string)