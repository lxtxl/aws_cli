#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-vpc-link.html
if __name__ == '__main__':
    """
	delete-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-vpc-link.html
	get-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-vpc-link.html
	get-vpc-links : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-vpc-links.html
	update-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-vpc-link.html
    """

    parameter_display_string = """
    # name : [Required] The name used to label and identify the VPC link.
    # target-arns : [Required] The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS account of the API owner.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "create-vpc-link", "name", "target-arns", add_option_dict)
