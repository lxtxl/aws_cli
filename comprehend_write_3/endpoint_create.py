#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-endpoint.html
if __name__ == '__main__':
    """
	delete-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-endpoint.html
	describe-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-endpoint.html
	list-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-endpoints.html
	update-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/update-endpoint.html
    """

    parameter_display_string = """
    # endpoint-name : This is the descriptive suffix that becomes part of the EndpointArn used for all subsequent requests to this resource.
    # model-arn : The Amazon Resource Number (ARN) of the model to which the endpoint will be attached.
    # desired-inference-units : The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("comprehend", "create-endpoint", "endpoint-name", "model-arn", "desired-inference-units", add_option_dict)
