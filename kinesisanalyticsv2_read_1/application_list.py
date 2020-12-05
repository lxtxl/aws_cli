#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/describe-application.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/create-application.html
	delete-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/delete-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/list-applications.html
	start-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/start-application.html
	stop-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/stop-application.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/update-application.html
    """

    parameter_display_string = """
    # application-name : The name of the application.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("kinesisanalyticsv2", "describe-application", "application-name", add_option_dict)