#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint.html
if __name__ == '__main__':
    """
	delete-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-endpoint.html
	describe-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-endpoint.html
	list-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-endpoints.html
	update-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-endpoint.html
    """

    parameter_display_string = """
    # endpoint-name : The name of the endpoint.The name must be unique within an AWS Region in your AWS account. The name is case-insensitive in CreateEndpoint , but the case is preserved and must be matched in .
    # endpoint-config-name : The name of an endpoint configuration. For more information, see  CreateEndpointConfig .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-endpoint", "endpoint-name", "endpoint-config-name", add_option_dict)
