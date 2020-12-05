#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-workflow-run.html
if __name__ == '__main__':
    """
	get-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run.html
	get-workflow-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-runs.html
	resume-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/resume-workflow-run.html
	start-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-workflow-run.html
    """

    parameter_display_string = """
    # name : The name of the workflow to stop.
    # run-id : The ID of the workflow run to stop.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "stop-workflow-run", "name", "run-id", add_option_dict)
