#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-image-version.html
if __name__ == '__main__':
    """
	create-image-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-image-version.html
	describe-image-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-image-version.html
	list-image-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-image-versions.html
    """

    parameter_display_string = """
    # image-name : The name of the image.
    # version-number : The version to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "delete-image-version", "image-name", "version-number", add_option_dict)
