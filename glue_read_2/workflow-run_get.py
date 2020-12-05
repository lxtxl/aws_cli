#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run.html
if __name__ == '__main__':
    """
	get-workflow-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-runs.html
	resume-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/resume-workflow-run.html
	start-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-workflow-run.html
	stop-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-workflow-run.html
    """

    parameter_display_string = """
    # name : Name of the workflow being run.
    # run-id : The ID of the workflow run.
    """

    execute_two_parameter("glue", "get-workflow-run", "name", "run-id", parameter_display_string)