#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-dataflow-endpoint-group.html
if __name__ == '__main__':
    """
	create-dataflow-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-dataflow-endpoint-group.html
	delete-dataflow-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/delete-dataflow-endpoint-group.html
	list-dataflow-endpoint-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-dataflow-endpoint-groups.html
    """

    parameter_display_string = """
    # dataflow-endpoint-group-id : UUID of a dataflow endpoint group.
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

    execute_one_parameter("groundstation", "get-dataflow-endpoint-group", "dataflow-endpoint-group-id", add_option_dict)