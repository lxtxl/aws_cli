#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-segment-detection.html
if __name__ == '__main__':
    """
	get-segment-detection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-segment-detection.html
    """

    parameter_display_string = """
    # video : 
    # segment-types : An array of segment types to detect in the video. Valid values are TECHNICAL_CUE and SHOT.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rekognition", "start-segment-detection", "video", "segment-types", add_option_dict)
