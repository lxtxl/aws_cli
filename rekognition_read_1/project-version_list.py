#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-project-versions.html
if __name__ == '__main__':
    """
	create-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-project-version.html
	delete-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-project-version.html
	start-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-project-version.html
	stop-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/stop-project-version.html
    """

    parameter_display_string = """
    # project-arn : The Amazon Resource Name (ARN) of the project that contains the models you want to describe.
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

    execute_one_parameter("rekognition", "describe-project-versions", "project-arn", add_option_dict)