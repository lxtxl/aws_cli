#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/delete-application-input-processing-configuration.html
if __name__ == '__main__':
    """
	add-application-input-processing-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/add-application-input-processing-configuration.html
    """

    parameter_display_string = """
    # application-name : The name of the application.
    # current-application-version-id : 
    # input-id : The ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the  DescribeApplication operation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesisanalyticsv2", "delete-application-input-processing-configuration", "application-name", "current-application-version-id", "input-id", add_option_dict)
