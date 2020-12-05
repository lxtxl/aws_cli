#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-trigger.html
if __name__ == '__main__':
    """
	create-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-trigger.html
	delete-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-trigger.html
	get-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-triggers.html
	list-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-triggers.html
	start-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-trigger.html
	stop-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-trigger.html
	update-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-trigger.html
    """

    parameter_display_string = """
    # name : The name of the trigger to retrieve.
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

    execute_one_parameter("glue", "get-trigger", "name", add_option_dict)