#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/flush-stage-cache.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # stage-name : [Required] The name of the stage to flush its cache.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "flush-stage-cache", "rest-api-id", "stage-name", add_option_dict)
