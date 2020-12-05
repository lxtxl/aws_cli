#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image-recipe.html
if __name__ == '__main__':
    """
	create-image-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-recipe.html
	get-image-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-recipe.html
	list-image-recipes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-recipes.html
    """

    parameter_display_string = """
    # image-recipe-arn : The Amazon Resource Name (ARN) of the image recipe to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("imagebuilder", "delete-image-recipe", "image-recipe-arn", add_option_dict)





