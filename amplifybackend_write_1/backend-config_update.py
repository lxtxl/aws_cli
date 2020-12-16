#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/update-backend-config.html
if __name__ == '__main__':
    """
	create-backend-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-backend-config.html
	remove-backend-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/remove-backend-config.html
    """

    parameter_display_string = """
    # app-id : The app ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("amplifybackend", "update-backend-config", "app-id", add_option_dict)





