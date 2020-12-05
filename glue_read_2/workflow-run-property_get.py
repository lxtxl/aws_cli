#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run-properties.html
if __name__ == '__main__':
    """
	put-workflow-run-properties : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/put-workflow-run-properties.html
    """

    parameter_display_string = """
    # name : Name of the workflow which was run.
    # run-id : The ID of the workflow run whose run properties should be returned.
    """

    execute_two_parameter("glue", "get-workflow-run-properties", "name", "run-id", parameter_display_string)