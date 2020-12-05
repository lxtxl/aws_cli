#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image.html
if __name__ == '__main__':
    """
	create-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html
	get-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image.html
	list-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html
    """

    parameter_display_string = """
    # image-build-version-arn : The Amazon Resource Name (ARN) of the image to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("imagebuilder", "delete-image", "image-build-version-arn", add_option_dict)





