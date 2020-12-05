#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-simulation-application.html
if __name__ == '__main__':
    """
	create-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-simulation-application.html
	describe-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-application.html
	list-simulation-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-applications.html
	update-simulation-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-simulation-application.html
    """

    parameter_display_string = """
    # application : The application information for the simulation application to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "delete-simulation-application", "application", add_option_dict)





