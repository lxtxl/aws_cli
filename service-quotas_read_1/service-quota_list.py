#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-service-quotas.html
if __name__ == '__main__':
    """
	get-service-quota : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-service-quota.html
    """

    parameter_display_string = """
    # service-code : The identifier for a service. When performing an operation, use the ServiceCode to specify a particular service.
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

    execute_one_parameter("service-quotas", "list-service-quotas", "service-code", add_option_dict)