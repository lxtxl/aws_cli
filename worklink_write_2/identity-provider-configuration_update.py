#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/update-identity-provider-configuration.html
if __name__ == '__main__':
    """
	describe-identity-provider-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-identity-provider-configuration.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    # identity-provider-type : The type of identity provider.
Possible values:

SAML
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("worklink", "update-identity-provider-configuration", "fleet-arn", "identity-provider-type", add_option_dict)
