#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint.html
if __name__ == '__main__':
    """
	create-vpc-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html
	delete-vpc-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoints.html
	describe-vpc-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoints.html
    """

    parameter_display_string = """
    # vpc-endpoint-id : The ID of the endpoint.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "modify-vpc-endpoint", "vpc-endpoint-id", add_option_dict)





