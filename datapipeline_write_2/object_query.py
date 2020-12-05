#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/query-objects.html
if __name__ == '__main__':
    """
	describe-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-objects.html
    """

    parameter_display_string = """
    # pipeline-id : The ID of the pipeline.
    # sphere : Indicates whether the query applies to components or instances. The possible values are: COMPONENT , INSTANCE , and ATTEMPT .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datapipeline", "query-objects", "pipeline-id", "sphere", add_option_dict)
