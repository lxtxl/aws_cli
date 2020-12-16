#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/put-workflow-run-properties.html
if __name__ == '__main__':
    """
	get-workflow-run-properties : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run-properties.html
    """

    parameter_display_string = """
    # name : Name of the workflow which was run.
    # run-id : The ID of the workflow run for which the run properties should be updated.
    # run-properties : The properties to put for the specified run.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "put-workflow-run-properties", "name", "run-id", "run-properties", add_option_dict)
