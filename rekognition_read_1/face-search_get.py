#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-face-search.html
if __name__ == '__main__':
    """
	start-face-search : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-face-search.html
    """

    parameter_display_string = """
    # job-id : The job identifer for the search request. You get the job identifier from an initial call to StartFaceSearch .
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

    execute_one_parameter("rekognition", "get-face-search", "job-id", add_option_dict)