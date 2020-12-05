#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-container-instances-state.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # container-instances : A list of container instance IDs or full ARN entries.
(string)
    # status : The container instance state with which to update the container instance. The only valid values for this action are ACTIVE and DRAINING . A container instance can only be updated to DRAINING status once it has reached an ACTIVE state. If a container instance is in REGISTERING , DEREGISTERING , or REGISTRATION_FAILED state you can describe the container instance but will be unable to update the container instance state.
Possible values:

ACTIVE
DRAINING
REGISTERING
DEREGISTERING
REGISTRATION_FAILED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecs", "update-container-instances-state", "container-instances", "status", add_option_dict)
