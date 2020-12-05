#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-image-permissions.html
if __name__ == '__main__':
    """
	describe-image-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-image-permissions.html
	update-image-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-image-permissions.html
    """

    parameter_display_string = """
    # name : The name of the private image.
    # shared-account-id : The 12-digit identifier of the AWS account for which to delete image permissions.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appstream", "delete-image-permissions", "name", "shared-account-id", add_option_dict)
