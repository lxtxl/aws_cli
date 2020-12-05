#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-job-run.html
if __name__ == '__main__':
    """
	get-job-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job-run.html
	get-job-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job-runs.html
    """

    parameter_display_string = """
    # job-name : The name of the job definition to use.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "start-job-run", "job-name", add_option_dict)





