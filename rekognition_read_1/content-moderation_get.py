#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-content-moderation.html
if __name__ == '__main__':
    """
	start-content-moderation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-content-moderation.html
    """

    parameter_display_string = """
    # job-id : The identifier for the unsafe content job. Use JobId to identify the job in a subsequent call to GetContentModeration .
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

    execute_one_parameter("rekognition", "get-content-moderation", "job-id", add_option_dict)