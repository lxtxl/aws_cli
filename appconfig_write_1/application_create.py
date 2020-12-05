#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-application.html
if __name__ == '__main__':
    """
	delete-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-application.html
	get-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-applications.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-application.html
    """

    parameter_display_string = """
    # name : A name for the application.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appconfig", "create-application", "name", add_option_dict)





