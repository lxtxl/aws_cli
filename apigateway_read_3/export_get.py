#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-export.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # stage-name : [Required] The name of the  Stage that will be exported.
    """

    execute_two_parameter("apigateway", "get-export", "rest-api-id", "stage-name", parameter_display_string)