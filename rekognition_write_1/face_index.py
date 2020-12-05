#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index-faces.html
if __name__ == '__main__':
    """
	compare-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/compare-faces.html
	delete-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-faces.html
	detect-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-faces.html
	list-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-faces.html
	search-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces.html
    """

    parameter_display_string = """
    # collection-id : The ID of an existing collection to which you want to add the faces that are detected in the input images.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rekognition", "index-faces", "collection-id", add_option_dict)





