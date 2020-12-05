#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-flow.html
if __name__ == '__main__':
    """
	create-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-flow.html
	delete-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/delete-flow.html
	list-flows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/list-flows.html
	start-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/start-flow.html
	stop-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/stop-flow.html
	update-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/update-flow.html
    """

    parameter_display_string = """
    # flow-name : The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only.
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

    execute_one_parameter("appflow", "describe-flow", "flow-name", add_option_dict)