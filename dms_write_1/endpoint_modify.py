#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-endpoint.html
if __name__ == '__main__':
    """
	create-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html
	delete-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-endpoint.html
	describe-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-endpoints.html
    """

    parameter_display_string = """
    # endpoint-arn : The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dms", "modify-endpoint", "endpoint-arn", add_option_dict)





