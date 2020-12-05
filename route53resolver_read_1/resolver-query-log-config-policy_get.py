#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config-policy.html
if __name__ == '__main__':
    """
	put-resolver-query-log-config-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/put-resolver-query-log-config-policy.html
    """

    parameter_display_string = """
    # arn : The ARN of the query logging configuration that you want to get the query logging policy for.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("route53resolver", "get-resolver-query-log-config-policy", "arn", add_option_dict)