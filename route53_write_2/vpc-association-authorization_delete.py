#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-vpc-association-authorization.html
if __name__ == '__main__':
    """
	create-vpc-association-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-vpc-association-authorization.html
	list-vpc-association-authorizations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-vpc-association-authorizations.html
    """

    parameter_display_string = """
    # hosted-zone-id : When removing authorization to associate a VPC that was created by one AWS account with a hosted zone that was created with a different AWS account, the ID of the hosted zone.
    # vpc : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "delete-vpc-association-authorization", "hosted-zone-id", "vpc", add_option_dict)
