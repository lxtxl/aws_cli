#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-build.html
if __name__ == '__main__':
    """
	create-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-build.html
	describe-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-build.html
	list-builds : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-builds.html
	update-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-build.html
	upload-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/upload-build.html
    """

    parameter_display_string = """
    # build-id : A unique identifier for a build to delete. You can use either the build ID or ARN value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "delete-build", "build-id", add_option_dict)





