#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot.html
if __name__ == '__main__':
    """
	create-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-robot.html
	deregister-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/deregister-robot.html
	describe-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot.html
	list-robots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robots.html
	register-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/register-robot.html
    """

    parameter_display_string = """
    # robot : The Amazon Resource Name (ARN) of the robot.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "delete-robot", "robot", add_option_dict)





