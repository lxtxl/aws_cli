#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/cancel-image-creation.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # image-build-version-arn : The Amazon Resource Name (ARN) of the image whose creation you want to cancel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("imagebuilder", "cancel-image-creation", "image-build-version-arn", add_option_dict)




