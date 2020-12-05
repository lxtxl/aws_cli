#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/put-pipeline-definition.html
if __name__ == '__main__':
    """
	get-pipeline-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/get-pipeline-definition.html
	validate-pipeline-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/validate-pipeline-definition.html
    """

    parameter_display_string = """
    # pipeline-id : The ID of the pipeline.
    # pipeline-definition : The JSON pipeline definition. If the pipeline definition is in a file you can use the file://syntax to specify a filename.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datapipeline", "put-pipeline-definition", "pipeline-id", "pipeline-definition", add_option_dict)
