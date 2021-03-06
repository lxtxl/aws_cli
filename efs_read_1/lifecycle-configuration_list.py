#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-lifecycle-configuration.html
if __name__ == '__main__':
    """
	put-lifecycle-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html
    """

    parameter_display_string = """
    # file-system-id : The ID of the file system whose LifecycleConfiguration object you want to retrieve (String).
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

    execute_one_parameter("efs", "describe-lifecycle-configuration", "file-system-id", add_option_dict)