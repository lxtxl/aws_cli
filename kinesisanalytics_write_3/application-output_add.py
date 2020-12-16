#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/add-application-output.html
if __name__ == '__main__':
    """
	delete-application-output : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/delete-application-output.html
    """

    parameter_display_string = """
    # application-name : Name of the application to which you want to add the output configuration.
    # current-application-version-id : 
    # application-output : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesisanalytics", "add-application-output", "application-name", "current-application-version-id", "application-output", add_option_dict)
