#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/copy-image.html
if __name__ == '__main__':
    """
	delete-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-image.html
	describe-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-images.html
    """

    parameter_display_string = """
    # source-image-name : The name of the image to copy.
    # destination-image-name : The name that the image will have when it is copied to the destination.
    # destination-region : The destination region to which the image will be copied. This parameter is required, even if you are copying an image within the same region.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appstream", "copy-image", "source-image-name", "destination-image-name", "destination-region", add_option_dict)
