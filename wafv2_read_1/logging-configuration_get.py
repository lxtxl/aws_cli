#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-logging-configuration.html
if __name__ == '__main__':
    """
	delete-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-logging-configuration.html
	list-logging-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-logging-configurations.html
	put-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/put-logging-configuration.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the web ACL for which you want to get the  LoggingConfiguration .
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

    execute_one_parameter("wafv2", "get-logging-configuration", "resource-arn", add_option_dict)