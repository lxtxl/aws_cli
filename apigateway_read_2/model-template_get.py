#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-model-template.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # model-name : [Required] The name of the model for which to generate a template.
    """

    execute_two_parameter("apigateway", "get-model-template", "rest-api-id", "model-name", parameter_display_string)