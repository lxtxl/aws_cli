#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/add-application-reference-data-source.html
if __name__ == '__main__':
    """
	delete-application-reference-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/delete-application-reference-data-source.html
    """

    parameter_display_string = """
    # application-name : Name of an existing application.
    # current-application-version-id : 
    # reference-data-source : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesisanalytics", "add-application-reference-data-source", "application-name", "current-application-version-id", "reference-data-source", add_option_dict)
