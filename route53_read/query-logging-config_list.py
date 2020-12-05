#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-query-logging-configs.html
if __name__ == '__main__':
    """
	create-query-logging-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-query-logging-config.html
	delete-query-logging-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-query-logging-config.html
	get-query-logging-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-query-logging-config.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("route53", "list-query-logging-configs", add_option_dict)