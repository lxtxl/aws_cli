#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html
if __name__ == '__main__':
    """
	delete-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image.html
	get-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image.html
	list-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html
    """

    parameter_display_string = """
    # image-recipe-arn : The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
    # infrastructure-configuration-arn : The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("imagebuilder", "create-image", "image-recipe-arn", "infrastructure-configuration-arn", add_option_dict)
