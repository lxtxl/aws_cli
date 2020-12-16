#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/upload-build.html
if __name__ == '__main__':
    """
	create-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-build.html
	delete-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-build.html
	describe-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-build.html
	list-builds : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-builds.html
	update-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-build.html
    """

    parameter_display_string = """
    # name : The name of the build
    # build-version : The version of the build
    # build-root : The path to the directory containing the build to upload
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("gamelift", "upload-build", "name", "build-version", "build-root", add_option_dict)
