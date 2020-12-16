#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/delete-application-vpc-configuration.html
if __name__ == '__main__':
    """
	add-application-vpc-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/add-application-vpc-configuration.html
    """

    parameter_display_string = """
    # application-name : The name of an existing application.
    # current-application-version-id : 
    # vpc-configuration-id : The ID of the VPC configuration to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesisanalyticsv2", "delete-application-vpc-configuration", "application-name", "current-application-version-id", "vpc-configuration-id", add_option_dict)
