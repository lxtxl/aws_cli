#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-query-log-config.html
if __name__ == '__main__':
    """
	create-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-query-log-config.html
	delete-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-query-log-config.html
	disassociate-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-query-log-config.html
	get-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config.html
	list-resolver-query-log-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-configs.html
    """

    parameter_display_string = """
    # resolver-query-log-config-id : The ID of the query logging configuration that you want to associate a VPC with.
    # resource-id : The ID of an Amazon VPC that you want this query logging configuration to log queries for.

Note
The VPCs and the query logging configuration must be in the same Region.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53resolver", "associate-resolver-query-log-config", "resolver-query-log-config-id", "resource-id", add_option_dict)
