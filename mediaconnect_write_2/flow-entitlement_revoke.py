#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/revoke-flow-entitlement.html
if __name__ == '__main__':
    """
	grant-flow-entitlements : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/grant-flow-entitlements.html
	update-flow-entitlement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-entitlement.html
    """

    parameter_display_string = """
    # entitlement-arn : The ARN of the entitlement that you want to revoke.
    # flow-arn : The flow that you want to revoke an entitlement from.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconnect", "revoke-flow-entitlement", "entitlement-arn", "flow-arn", add_option_dict)
