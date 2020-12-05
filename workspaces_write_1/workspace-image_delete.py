#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-workspace-image.html
if __name__ == '__main__':
    """
	copy-workspace-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/copy-workspace-image.html
	describe-workspace-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-images.html
	import-workspace-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/import-workspace-image.html
    """

    parameter_display_string = """
    # image-id : The identifier of the image.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workspaces", "delete-workspace-image", "image-id", add_option_dict)





