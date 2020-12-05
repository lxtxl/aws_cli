#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-runs.html
if __name__ == '__main__':
    """
	get-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run.html
	resume-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/resume-workflow-run.html
	start-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-workflow-run.html
	stop-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-workflow-run.html
    """

    parameter_display_string = """
    # name : Name of the workflow whose metadata of runs should be returned.
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

    execute_one_parameter("glue", "get-workflow-runs", "name", add_option_dict)