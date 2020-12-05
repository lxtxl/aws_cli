#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/create-preset.html
if __name__ == '__main__':
    """
	delete-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/delete-preset.html
	list-presets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-presets.html
	read-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/read-preset.html
    """

    parameter_display_string = """
    # name : The name of the preset. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.
    # container : The container type for the output file. Valid values include flac , flv , fmp4 , gif , mp3 , mp4 , mpg , mxf , oga , ogg , ts , and webm .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elastictranscoder", "create-preset", "name", "container", add_option_dict)
