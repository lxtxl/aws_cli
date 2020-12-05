#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image.html
if __name__ == '__main__':
    """
	create-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html
	delete-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image.html
	list-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html
    """

    parameter_display_string = """
    # image-build-version-arn : The Amazon Resource Name (ARN) of the image that you want to retrieve.
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

    execute_one_parameter("imagebuilder", "get-image", "image-build-version-arn", add_option_dict)