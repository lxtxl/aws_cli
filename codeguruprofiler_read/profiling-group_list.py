#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-profiling-groups.html
if __name__ == '__main__':
    """
	create-profiling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/create-profiling-group.html
	delete-profiling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/delete-profiling-group.html
	describe-profiling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/describe-profiling-group.html
	update-profiling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/update-profiling-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("codeguruprofiler", "list-profiling-groups", add_option_dict)