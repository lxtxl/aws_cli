#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/create-packaging-configuration.html
if __name__ == '__main__':
    """
	delete-packaging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/delete-packaging-configuration.html
	describe-packaging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-packaging-configuration.html
	list-packaging-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-packaging-configurations.html
    """

    parameter_display_string = """
    # id : The ID of the PackagingConfiguration.
    # packaging-group-id : The ID of a PackagingGroup.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediapackage-vod", "create-packaging-configuration", "id", "packaging-group-id", add_option_dict)
