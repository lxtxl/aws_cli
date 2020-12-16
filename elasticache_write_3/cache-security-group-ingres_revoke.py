#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/revoke-cache-security-group-ingress.html
if __name__ == '__main__':
    """
	authorize-cache-security-group-ingress : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/authorize-cache-security-group-ingress.html
    """

    parameter_display_string = """
    # cache-security-group-name : The name of the cache security group to revoke ingress from.
    # ec2-security-group-name : The name of the Amazon EC2 security group to revoke access from.
    # ec2-security-group-owner-id : The AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("elasticache", "revoke-cache-security-group-ingress", "cache-security-group-name", "ec2-security-group-name", "ec2-security-group-owner-id", add_option_dict)
