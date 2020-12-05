#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/create-application.html
if __name__ == '__main__':
    """
	delete-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/delete-applications.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/update-application.html
    """

    parameter_display_string = """
    # name : Name of the application to be created.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("discovery", "create-application", "name", add_option_dict)





