#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-stop-job-run.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-name : The name of the job definition for which to stop job runs.
    # job-run-ids : A list of the JobRunIds that should be stopped for that job definition.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "batch-stop-job-run", "job-name", "job-run-ids", add_option_dict)
