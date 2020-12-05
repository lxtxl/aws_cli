#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-dev-endpoint.html
if __name__ == '__main__':
    """
	delete-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-dev-endpoint.html
	get-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoint.html
	get-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoints.html
	list-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-dev-endpoints.html
	update-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-dev-endpoint.html
    """

    parameter_display_string = """
    # endpoint-name : The name to be assigned to the new DevEndpoint .
    # role-arn : The IAM role for the DevEndpoint .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "create-dev-endpoint", "endpoint-name", "role-arn", add_option_dict)
