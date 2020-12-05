#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-archive.html
if __name__ == '__main__':
    """
	create-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-archive.html
	delete-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-archive.html
	list-archives : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-archives.html
	update-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/update-archive.html
    """

    parameter_display_string = """
    # archive-name : The name of the archive to retrieve.
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

    execute_one_parameter("events", "describe-archive", "archive-name", add_option_dict)