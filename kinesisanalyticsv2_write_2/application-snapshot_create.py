#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/create-application-snapshot.html
if __name__ == '__main__':
    """
	delete-application-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/delete-application-snapshot.html
	describe-application-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/describe-application-snapshot.html
	list-application-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/list-application-snapshots.html
    """

    parameter_display_string = """
    # application-name : The name of an existing application
    # snapshot-name : An identifier for the application snapshot.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesisanalyticsv2", "create-application-snapshot", "application-name", "snapshot-name", add_option_dict)
