#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/delete-application-reference-data-source.html
if __name__ == '__main__':
    """
	add-application-reference-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/add-application-reference-data-source.html
    """

    parameter_display_string = """
    # application-name : The name of an existing application.
    # current-application-version-id : 
    # reference-id : The ID of the reference data source. When you add a reference data source to your application using the  AddApplicationReferenceDataSource , Kinesis Data Analytics assigns an ID. You can use the  DescribeApplication operation to get the reference ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesisanalyticsv2", "delete-application-reference-data-source", "application-name", "current-application-version-id", "reference-id", add_option_dict)
