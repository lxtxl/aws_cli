#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/create-endpoint.html
if __name__ == '__main__':
    """
	delete-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/delete-endpoint.html
	list-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/list-endpoints.html
    """

    parameter_display_string = """
    # outpost-id : The ID of the AWS Outpost.
    # subnet-id : The ID of the subnet in the selected VPC.
    # security-group-id : The ID of the security group to use with the endpoint.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3outposts", "create-endpoint", "outpost-id", "subnet-id", "security-group-id", add_option_dict)
