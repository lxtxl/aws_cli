#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-account-limit.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # type : The limit that you want to get. Valid values include the following:

MAX_HEALTH_CHECKS_BY_OWNER : The maximum number of health checks that you can create using the current account.
MAX_HOSTED_ZONES_BY_OWNER : The maximum number of hosted zones that you can create using the current account.
MAX_REUSABLE_DELEGATION_SETS_BY_OWNER : The maximum number of reusable delegation sets that you can create using the current account.
MAX_TRAFFIC_POLICIES_BY_OWNER : The maximum number of traffic policies that you can create using the current account.
MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER : The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)

Possible values:

MAX_HEALTH_CHECKS_BY_OWNER
MAX_HOSTED_ZONES_BY_OWNER
MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER
MAX_REUSABLE_DELEGATION_SETS_BY_OWNER
MAX_TRAFFIC_POLICIES_BY_OWNER
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

    execute_one_parameter("route53", "get-account-limit", "type", add_option_dict)