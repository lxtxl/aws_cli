#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/delete-endpoint.html
if __name__ == '__main__':
    """
	create-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/create-endpoint.html
	list-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/list-endpoints.html
    """

    parameter_display_string = """
    # endpoint-id : The ID of the end point.
    # outpost-id : The ID of the AWS Outpost.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3outposts", "delete-endpoint", "endpoint-id", "outpost-id", add_option_dict)
