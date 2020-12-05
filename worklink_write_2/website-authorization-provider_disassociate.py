#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/disassociate-website-authorization-provider.html
if __name__ == '__main__':
    """
	associate-website-authorization-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-website-authorization-provider.html
	list-website-authorization-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-website-authorization-providers.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    # authorization-provider-id : A unique identifier for the authorization provider.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("worklink", "disassociate-website-authorization-provider", "fleet-arn", "authorization-provider-id", add_option_dict)
