#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-endpoint.html
if __name__ == '__main__':
    """
	create-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint.html
	describe-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-endpoint.html
	list-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-endpoints.html
	update-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-endpoint.html
    """

    parameter_display_string = """
    # endpoint-name : The name of the endpoint that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-endpoint", "endpoint-name", add_option_dict)





