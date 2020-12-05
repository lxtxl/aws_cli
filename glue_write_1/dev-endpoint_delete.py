#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-dev-endpoint.html
if __name__ == '__main__':
    """
	create-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-dev-endpoint.html
	get-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoint.html
	get-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoints.html
	list-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-dev-endpoints.html
	update-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-dev-endpoint.html
    """

    parameter_display_string = """
    # endpoint-name : The name of the DevEndpoint .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "delete-dev-endpoint", "endpoint-name", add_option_dict)





