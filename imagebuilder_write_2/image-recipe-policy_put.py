#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/put-image-recipe-policy.html
if __name__ == '__main__':
    """
	get-image-recipe-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-recipe-policy.html
    """

    parameter_display_string = """
    # image-recipe-arn : The Amazon Resource Name (ARN) of the image recipe that this policy should be applied to.
    # policy : The policy to apply.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("imagebuilder", "put-image-recipe-policy", "image-recipe-arn", "policy", add_option_dict)
