#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-environment.html
if __name__ == '__main__':
    """
	delete-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-environment.html
	get-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-environment.html
	list-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-environments.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-environment.html
    """

    parameter_display_string = """
    # application-id : The application ID.
    # name : A name for the environment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appconfig", "create-environment", "application-id", "name", add_option_dict)
