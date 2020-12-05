#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces.html
if __name__ == '__main__':
    """
	compare-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/compare-faces.html
	delete-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-faces.html
	detect-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-faces.html
	index-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index-faces.html
	list-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-faces.html
    """

    parameter_display_string = """
    # collection-id : ID of the collection the face belongs to.
    # face-id : ID of a face to find matches for in the collection.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rekognition", "search-faces", "collection-id", "face-id", add_option_dict)
