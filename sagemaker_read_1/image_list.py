#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-image.html
if __name__ == '__main__':
    """
	create-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-image.html
	delete-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-image.html
	list-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-images.html
	update-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-image.html
    """

    parameter_display_string = """
    # image-name : The name of the image to describe.
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

    execute_one_parameter("sagemaker", "describe-image", "image-name", add_option_dict)