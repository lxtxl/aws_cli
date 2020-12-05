#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-workflow-run.html
if __name__ == '__main__':
    """
	get-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run.html
	get-workflow-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-runs.html
	resume-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/resume-workflow-run.html
	stop-workflow-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-workflow-run.html
    """

    parameter_display_string = """
    # name : The name of the workflow to start.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "start-workflow-run", "name", add_option_dict)





