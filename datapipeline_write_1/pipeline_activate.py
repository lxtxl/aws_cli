#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/activate-pipeline.html
if __name__ == '__main__':
    """
	create-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/create-pipeline.html
	deactivate-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/deactivate-pipeline.html
	delete-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/delete-pipeline.html
	describe-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-pipelines.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-pipelines.html
    """

    parameter_display_string = """
    # pipeline-id : The ID of the pipeline.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("datapipeline", "activate-pipeline", "pipeline-id", add_option_dict)





