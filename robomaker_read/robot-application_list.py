#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robot-applications.html
if __name__ == '__main__':
    """
	create-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-robot-application.html
	delete-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot-application.html
	describe-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot-application.html
	update-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-robot-application.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("robomaker", "list-robot-applications", add_option_dict)