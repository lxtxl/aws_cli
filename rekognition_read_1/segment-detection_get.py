#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-segment-detection.html
if __name__ == '__main__':
    """
	start-segment-detection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-segment-detection.html
    """

    parameter_display_string = """
    # job-id : Job identifier for the text detection operation for which you want results returned. You get the job identifer from an initial call to StartSegmentDetection .
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

    execute_one_parameter("rekognition", "get-segment-detection", "job-id", add_option_dict)