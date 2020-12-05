#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-faces.html
if __name__ == '__main__':
    """
	compare-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/compare-faces.html
	delete-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-faces.html
	detect-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-faces.html
	index-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index-faces.html
	search-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces.html
    """

    parameter_display_string = """
    # collection-id : ID of the collection from which to list the faces.
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

    execute_one_parameter("rekognition", "list-faces", "collection-id", add_option_dict)