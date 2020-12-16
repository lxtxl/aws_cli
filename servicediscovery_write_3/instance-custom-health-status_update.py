#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-instance-custom-health-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # service-id : The ID of the service that includes the configuration for the custom health check that you want to change the status for.
    # instance-id : The ID of the instance that you want to change the health status for.
    # status : The new status of the instance, HEALTHY or UNHEALTHY .
Possible values:

HEALTHY
UNHEALTHY
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("servicediscovery", "update-instance-custom-health-status", "service-id", "instance-id", "status", add_option_dict)
