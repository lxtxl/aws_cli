#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-export-labels-task-run.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # transform-id : The unique identifier of the machine learning transform.
    # output-s3-path : The Amazon S3 path where you export the labels.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "start-export-labels-task-run", "transform-id", "output-s3-path", add_option_dict)
