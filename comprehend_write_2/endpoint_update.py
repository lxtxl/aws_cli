#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/update-endpoint.html
if __name__ == '__main__':
    """
	create-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-endpoint.html
	delete-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-endpoint.html
	describe-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-endpoint.html
	list-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-endpoints.html
    """

    parameter_display_string = """
    # endpoint-arn : The Amazon Resource Number (ARN) of the endpoint being updated.
    # desired-inference-units : The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("comprehend", "update-endpoint", "endpoint-arn", "desired-inference-units", add_option_dict)
