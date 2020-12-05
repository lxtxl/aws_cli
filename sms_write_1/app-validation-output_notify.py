#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/notify-app-validation-output.html
if __name__ == '__main__':
    """
	get-app-validation-output : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/get-app-validation-output.html
    """

    parameter_display_string = """
    # app-id : The ID of the application.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sms", "notify-app-validation-output", "app-id", add_option_dict)





