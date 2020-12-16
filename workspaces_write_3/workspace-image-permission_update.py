#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/update-workspace-image-permission.html
if __name__ == '__main__':
    """
	describe-workspace-image-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-image-permissions.html
    """

    parameter_display_string = """
    # image-id : The identifier of the image.
    # allow-copy-image | --no-allow-copy-image : The permission to copy the image. This permission can be revoked only after an image has been shared.
    # shared-account-id : The identifier of the AWS account to share or unshare the image with.

Warning
Before sharing the image, confirm that you are sharing to the correct AWS account ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workspaces", "update-workspace-image-permission", "image-id", "allow-copy-image | --no-allow-copy-image", "shared-account-id", add_option_dict)
