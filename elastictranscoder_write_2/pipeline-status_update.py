#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/update-pipeline-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # id : The identifier of the pipeline to update.
    # status : The desired status of the pipeline:

Active : The pipeline is processing jobs.
Paused : The pipeline is not currently processing jobs.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elastictranscoder", "update-pipeline-status", "id", "status", add_option_dict)
