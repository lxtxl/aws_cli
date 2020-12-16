#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/copy-workspace-image.html
if __name__ == '__main__':
    """
	delete-workspace-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-workspace-image.html
	describe-workspace-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-images.html
	import-workspace-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/import-workspace-image.html
    """

    parameter_display_string = """
    # name : The name of the image.
    # source-image-id : The identifier of the source image.
    # source-region : The identifier of the source Region.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workspaces", "copy-workspace-image", "name", "source-image-id", "source-region", add_option_dict)
