#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-runtime/invoke-endpoint.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # endpoint-name : The name of the endpoint that you specified when you created the endpoint using the CreateEndpoint API.
    # body : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker-runtime", "invoke-endpoint", "endpoint-name", "body", add_option_dict)
