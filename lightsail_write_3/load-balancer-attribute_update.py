#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/update-load-balancer-attribute.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer that you want to modify (e.g., my-load-balancer .
    # attribute-name : The name of the attribute you want to update. Valid values are below.
Possible values:

HealthCheckPath
SessionStickinessEnabled
SessionStickiness_LB_CookieDurationSeconds
    # attribute-value : The value that you want to specify for the attribute name.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lightsail", "update-load-balancer-attribute", "load-balancer-name", "attribute-name", "attribute-value", add_option_dict)
