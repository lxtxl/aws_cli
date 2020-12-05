#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-content-moderation.html
if __name__ == '__main__':
    """
	get-content-moderation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-content-moderation.html
    """

    parameter_display_string = """
    # video : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rekognition", "start-content-moderation", "video", add_option_dict)





