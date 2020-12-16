#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/delete-application-output.html
if __name__ == '__main__':
    """
	add-application-output : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/add-application-output.html
    """

    parameter_display_string = """
    # application-name : Amazon Kinesis Analytics application name.
    # current-application-version-id : 
    # output-id : The ID of the configuration to delete. Each output configuration that is added to the application, either when the application is created or later using the AddApplicationOutput operation, has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the DescribeApplication operation to get the specific OutputId .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesisanalytics", "delete-application-output", "application-name", "current-application-version-id", "output-id", add_option_dict)
