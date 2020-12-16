#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robots.html
if __name__ == '__main__':
    """
	create-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-robot.html
	delete-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot.html
	deregister-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/deregister-robot.html
	describe-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot.html
	register-robot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/register-robot.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("robomaker", "list-robots", add_option_dict)