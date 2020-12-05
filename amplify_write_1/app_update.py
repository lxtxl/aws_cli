#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/update-app.html
if __name__ == '__main__':
    """
	create-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-app.html
	delete-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-app.html
	get-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-app.html
	list-apps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-apps.html
    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("amplify", "update-app", "app-id", add_option_dict)





