#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/deregister-robot.html
if __name__ == '__main__':
    """
	create-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-robot.html
	delete-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot.html
	describe-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot.html
	list-robots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robots.html
	register-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/register-robot.html
    """

    parameter_display_string = """
    # fleet : The Amazon Resource Name (ARN) of the fleet.
    # robot : The Amazon Resource Name (ARN) of the robot.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("robomaker", "deregister-robot", "fleet", "robot", add_option_dict)
