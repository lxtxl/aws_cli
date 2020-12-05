#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-face-search.html
if __name__ == '__main__':
    """
	get-face-search : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-face-search.html
    """

    parameter_display_string = """
    # video : 
    # collection-id : ID of the collection that contains the faces you want to search for.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rekognition", "start-face-search", "video", "collection-id", add_option_dict)
