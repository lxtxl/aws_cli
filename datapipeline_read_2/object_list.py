#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-objects.html
if __name__ == '__main__':
    """
	query-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/query-objects.html
    """

    parameter_display_string = """
    # pipeline-id : The ID of the pipeline that contains the object definitions.
    # object-ids : The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to DescribeObjects .
(string)
    """

    execute_two_parameter("datapipeline", "describe-objects", "pipeline-id", "object-ids", parameter_display_string)