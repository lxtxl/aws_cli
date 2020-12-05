#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/stop-job-run.html
if __name__ == '__main__':
    """
	list-job-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-job-runs.html
	start-job-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/start-job-run.html
    """

    parameter_display_string = """
    # name : The name of the job to be stopped.
    # run-id : The ID of the job run to be stopped.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("databrew", "stop-job-run", "name", "run-id", add_option_dict)
