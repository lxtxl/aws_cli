#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/describe-profiling-group.html
if __name__ == '__main__':
    """
	create-profiling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/create-profiling-group.html
	delete-profiling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/delete-profiling-group.html
	list-profiling-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-profiling-groups.html
	update-profiling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/update-profiling-group.html
    """

    parameter_display_string = """
    # profiling-group-name : The name of the profiling group to get information about.
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

    execute_one_parameter("codeguruprofiler", "describe-profiling-group", "profiling-group-name", add_option_dict)