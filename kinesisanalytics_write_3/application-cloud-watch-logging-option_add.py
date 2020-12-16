#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/add-application-cloud-watch-logging-option.html
if __name__ == '__main__':
    """
	delete-application-cloud-watch-logging-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/delete-application-cloud-watch-logging-option.html
    """

    parameter_display_string = """
    # application-name : The Kinesis Analytics application name.
    # current-application-version-id : 
    # cloud-watch-logging-option : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesisanalytics", "add-application-cloud-watch-logging-option", "application-name", "current-application-version-id", "cloud-watch-logging-option", add_option_dict)
