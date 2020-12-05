#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-data-source.html
if __name__ == '__main__':
    """
	delete-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-data-source.html
	describe-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-data-sources.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-data-source.html
    """

    parameter_display_string = """
    # data-source-id : The ID assigned to the DataSource at creation.
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

    execute_one_parameter("machinelearning", "get-data-source", "data-source-id", add_option_dict)