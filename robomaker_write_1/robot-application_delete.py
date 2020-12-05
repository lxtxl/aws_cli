#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot-application.html
if __name__ == '__main__':
    """
	create-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-robot-application.html
	describe-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot-application.html
	list-robot-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robot-applications.html
	update-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-robot-application.html
    """

    parameter_display_string = """
    # application : The Amazon Resource Name (ARN) of the the robot application.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "delete-robot-application", "application", add_option_dict)





