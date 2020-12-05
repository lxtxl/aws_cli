#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/start-image-builder.html
if __name__ == '__main__':
    """
	create-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-image-builder.html
	delete-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-image-builder.html
	describe-image-builders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-image-builders.html
	stop-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/stop-image-builder.html
    """

    parameter_display_string = """
    # name : The name of the image builder.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appstream", "start-image-builder", "name", add_option_dict)





