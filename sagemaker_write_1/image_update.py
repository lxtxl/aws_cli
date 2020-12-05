#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-image.html
if __name__ == '__main__':
    """
	create-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-image.html
	delete-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-image.html
	describe-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-image.html
	list-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-images.html
    """

    parameter_display_string = """
    # image-name : The name of the image to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "update-image", "image-name", add_option_dict)





