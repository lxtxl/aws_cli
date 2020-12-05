#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-packaging-group.html
if __name__ == '__main__':
    """
	create-packaging-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/create-packaging-group.html
	delete-packaging-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/delete-packaging-group.html
	list-packaging-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-packaging-groups.html
	update-packaging-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/update-packaging-group.html
    """

    parameter_display_string = """
    # id : The ID of a MediaPackage VOD PackagingGroup resource.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("mediapackage-vod", "describe-packaging-group", "id", add_option_dict)