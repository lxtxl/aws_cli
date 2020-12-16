#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-robot-application.html
if __name__ == '__main__':
    """
	create-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-robot-application.html
	delete-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-robot-application.html
	describe-robot-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-robot-application.html
	list-robot-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-robot-applications.html
    """

    parameter_display_string = """
    # application : The application information for the robot application.
    # sources : The sources of the robot application.
(structure)

Information about a source configuration.
s3Bucket -> (string)

The Amazon S3 bucket name.

s3Key -> (string)

The s3 object key.

architecture -> (string)

The target processor architecture for the application.
    # robot-software-suite : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("robomaker", "update-robot-application", "application", "sources", "robot-software-suite", add_option_dict)
