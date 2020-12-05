#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config.html
if __name__ == '__main__':
    """
	associate-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-query-log-config.html
	create-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-query-log-config.html
	delete-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-query-log-config.html
	disassociate-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-query-log-config.html
	list-resolver-query-log-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-configs.html
    """

    parameter_display_string = """
    # resolver-query-log-config-id : The ID of the Resolver query logging configuration that you want to get information about.
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

    execute_one_parameter("route53resolver", "get-resolver-query-log-config", "resolver-query-log-config-id", add_option_dict)