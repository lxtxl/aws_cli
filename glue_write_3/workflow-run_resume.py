#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/resume-workflow-run.html
if __name__ == '__main__':
    """
	get-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run.html
	get-workflow-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-runs.html
	start-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-workflow-run.html
	stop-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-workflow-run.html
    """

    parameter_display_string = """
    # name : The name of the workflow to resume.
    # run-id : The ID of the workflow run to resume.
    # node-ids : A list of the node IDs for the nodes you want to restart. The nodes that are to be restarted must have a run attempt in the original run.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "resume-workflow-run", "name", "run-id", "node-ids", add_option_dict)
