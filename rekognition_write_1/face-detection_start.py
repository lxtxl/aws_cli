#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-face-detection.html
if __name__ == '__main__':
    """
	get-face-detection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-face-detection.html
    """

    parameter_display_string = """
    # video : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rekognition", "start-face-detection", "video", add_option_dict)





