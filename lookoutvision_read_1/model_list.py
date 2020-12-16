#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/list-models.html
if __name__ == '__main__':
    """
	create-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-model.html
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/delete-model.html
	describe-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-model.html
	start-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/start-model.html
	stop-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/stop-model.html
    """

    parameter_display_string = """
    # project-name : The name of the project that contains the model versions that you want to list.
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

    execute_one_parameter("lookoutvision", "list-models", "project-name", add_option_dict)