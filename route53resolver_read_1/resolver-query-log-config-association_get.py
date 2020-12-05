#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config-association.html
if __name__ == '__main__':
    """
	list-resolver-query-log-config-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-config-associations.html
    """

    parameter_display_string = """
    # resolver-query-log-config-association-id : The ID of the Resolver query logging configuration association that you want to get information about.
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

    execute_one_parameter("route53resolver", "get-resolver-query-log-config-association", "resolver-query-log-config-association-id", add_option_dict)