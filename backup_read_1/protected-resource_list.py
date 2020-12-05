#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-protected-resource.html
if __name__ == '__main__':
    """
	list-protected-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-protected-resources.html
    """

    parameter_display_string = """
    # resource-arn : An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
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

    execute_one_parameter("backup", "describe-protected-resource", "resource-arn", add_option_dict)