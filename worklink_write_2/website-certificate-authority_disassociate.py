#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/disassociate-website-certificate-authority.html
if __name__ == '__main__':
    """
	associate-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-website-certificate-authority.html
	describe-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-website-certificate-authority.html
	list-website-certificate-authorities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-website-certificate-authorities.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    # website-ca-id : A unique identifier for the CA.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("worklink", "disassociate-website-certificate-authority", "fleet-arn", "website-ca-id", add_option_dict)
