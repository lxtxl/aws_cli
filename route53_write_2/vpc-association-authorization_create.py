#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-vpc-association-authorization.html
if __name__ == '__main__':
    """
	delete-vpc-association-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-vpc-association-authorization.html
	list-vpc-association-authorizations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-vpc-association-authorizations.html
    """

    parameter_display_string = """
    # hosted-zone-id : The ID of the private hosted zone that you want to authorize associating a VPC with.
    # vpc : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "create-vpc-association-authorization", "hosted-zone-id", "vpc", add_option_dict)
