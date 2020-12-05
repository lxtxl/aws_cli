#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-builds.html
if __name__ == '__main__':
    """
	create-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-build.html
	delete-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-build.html
	describe-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-build.html
	update-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-build.html
	upload-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/upload-build.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("gamelift", "list-builds", add_option_dict)