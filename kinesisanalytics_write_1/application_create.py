#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/create-application.html
if __name__ == '__main__':
    """
	delete-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/delete-application.html
	describe-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/describe-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/list-applications.html
	start-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/start-application.html
	stop-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/stop-application.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/update-application.html
    """

    parameter_display_string = """
    # application-name : Name of your Amazon Kinesis Analytics application (for example, sample-app ).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kinesisanalytics", "create-application", "application-name", add_option_dict)





