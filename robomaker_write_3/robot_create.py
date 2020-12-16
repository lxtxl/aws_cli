#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-robot.html
if __name__ == '__main__':
    """
	delete-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot.html
	deregister-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/deregister-robot.html
	describe-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot.html
	list-robots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robots.html
	register-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/register-robot.html
    """

    parameter_display_string = """
    # name : The name for the robot.
    # architecture : The target architecture of the robot.
Possible values:

X86_64
ARM64
ARMHF
    # greengrass-group-id : The Greengrass group id.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("robomaker", "create-robot", "name", "architecture", "greengrass-group-id", add_option_dict)
