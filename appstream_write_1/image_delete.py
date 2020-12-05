#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-image.html
if __name__ == '__main__':
    """
	copy-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/copy-image.html
	describe-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-images.html
    """

    parameter_display_string = """
    # name : The name of the image.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appstream", "delete-image", "name", add_option_dict)





