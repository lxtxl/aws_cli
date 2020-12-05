#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-health-check-last-failure-reason.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # health-check-id : The ID for the health check for which you want the last failure reason. When you created the health check, CreateHealthCheck returned the ID in the response, in the HealthCheckId element.

Note
If you want to get the last failure reason for a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You canât use GetHealthCheckLastFailureReason for a calculated health check.
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

    execute_one_parameter("route53", "get-health-check-last-failure-reason", "health-check-id", add_option_dict)